# Use Python 3.12 slim as base
FROM python:3.12-slim

# Metadata
LABEL maintainer="jwilson@kloverdevs.ca"
LABEL org.opencontainers.image.title="sportly"
LABEL org.opencontainers.image.description="Python SDK for ESPN and NHL sports data"
LABEL org.opencontainers.image.source="https://github.com/pseudo-r/sportly"

# Don't buffer stdout/stderr
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Create app user (non-root)
RUN addgroup --system sportly && adduser --system --ingroup sportly sportly

WORKDIR /app

# Copy and install dependencies first (layer cache)
COPY pyproject.toml README.md ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

# Copy source
COPY sportly/ ./sportly/

# Switch to non-root user
USER sportly

# Default: show info
ENTRYPOINT ["sportly"]
CMD ["info"]
