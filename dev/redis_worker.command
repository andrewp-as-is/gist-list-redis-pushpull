#!/usr/bin/open -a Terminal
{ set +x; } 2>/dev/null

{ set -x; cd "${0%/*/*}"; { set +x; } 2>/dev/null; }

[ -e .env ] && { set -o allexport; . .env || exit; }

( set -x; python3 -u manage.py redis_worker )
