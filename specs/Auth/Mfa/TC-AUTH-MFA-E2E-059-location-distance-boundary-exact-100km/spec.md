---
id: TC-AUTH-MFA-E2E-059-location-distance-boundary-exact-100km
title: Nilai batas jarak anomali lokasi tepat 100km konsisten dengan ambang deteksi
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-18
coverage:
  web: automated
---

# Nilai batas jarak anomali lokasi tepat 100km konsisten dengan ambang deteksi

## Prerequisites

- Mode: mock
- Mode: mock (simulasi koordinat geografis tepat pada ambang batas 100km dari lokasi login terakhir)

## Test Steps

1. Simulasikan IP login dari koordinat tepat berjarak 100.0 km (≤100km)
2. Verifikasi sistem tidak memicu MFA karena masih memenuhi kondisi inklusif ambang batas aman
3. Simulasikan IP login dari koordinat berjarak 100.1 km (>100km)
4. Verifikasi sistem memicu MFA secara konsisten sesuai formula Haversine ambang batas >100km

## Notes

- TC Frontend Ref: `— (Manual di FE doc)`
- Merepresentasikan `TC-AUTH-MFA-18`.
