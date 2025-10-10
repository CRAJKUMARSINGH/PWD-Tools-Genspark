# Bridge GAD Git Tagging

This document explains how to create and push Git tags for Bridge GAD releases.

## Prerequisites

1. Git must be installed and available in your PATH
2. You must have push permissions to the remote repository
3. Your working directory should be clean (committed changes)

## Automatic Tagging

Run the provided script to automatically create and push a tag based on the current version:

```
create_git_tag.bat
```

This script will:
1. Extract the version from `src/bridge_gad/__init__.py`
2. Create a Git tag in the format `vX.Y.Z`
3. Push the tag to the origin repository

## Manual Tagging

If you prefer to create tags manually, follow these steps:

### 1. Create a tag locally

```bash
git tag v2.0.0
```

### 2. Push the tag to the remote repository

```bash
git push origin v2.0.0
```

### 3. Push all tags (optional)

```bash
git push origin --tags
```

## Versioning Strategy

Bridge GAD follows semantic versioning:
- **Major version** (X.y.z): Breaking changes
- **Minor version** (x.Y.z): New features
- **Patch version** (x.y.Z): Bug fixes

## Checking Tags

### List local tags

```bash
git tag
```

### List remote tags

```bash
git ls-remote --tags origin
```

## Deleting Tags

### Delete local tag

```bash
git tag -d v2.0.0
```

### Delete remote tag

```bash
git push origin --delete v2.0.0
```

## Best Practices

1. Always create tags after a successful build and test
2. Ensure version numbers are consistent across all files before tagging
3. Create release notes for each tag
4. Verify the tag was pushed successfully