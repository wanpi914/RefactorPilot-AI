# API Design

POST /review/pr
POST /review/snippet
POST /refactor
POST /security/scan
POST /architecture/analyze

Payload:
{
  "repo": "...",
  "diff": "...",
  "language": "python"
}
