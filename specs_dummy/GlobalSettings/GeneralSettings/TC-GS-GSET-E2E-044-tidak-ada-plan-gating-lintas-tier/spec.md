---
id: TC-GS-GSET-E2E-044-tidak-ada-plan-gating-lintas-tier
title: Tidak ada plan gating lintas-tier subscription
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-145
coverage:
  web: automated
---

# Tidak ada plan gating lintas tier subscription

## Prerequisites

- Environment menyediakan dua tenant dengan tier subscription berbeda (misal tier `Bronze` dan
  `Diamond`) tanpa perbedaan capability untuk modul ini.
- Offline tunning: gating plan dibuktikan tidak memengaruhi UI karena seluruh tier memiliki akses.

## Test Steps

1. Login sebagai admin pada tenant tier rendah (Bronze)
2. Buka `Global Settings > General Settings`
3. Verifikasi seluruh lima field dan tombol `[Save]` tampil normal
4. Verifikasi Modal Changelog dapat dibuka dan menampilkan riwayat penuh
5. Verifikasi tidak ada upsell/peringatan plan yang menghalangi penggunaan modul
6. Login pada tenant tier tinggi (Diamond)
7. Ulangi langkah 2-5
8. Bandingkan: tampilan, kapabilitas, dan data yang dapat diakses pada kedua tier identik
9. Verifikasi tidak ada gating tambahan pada download changelog / seluruh toolbar di kedua tier

## Notes

- Modul General Settings adalah entitas konfigurasi paylod, bukan entitas master data berkuota,
  sehingga PMC `PLAN-GATING` tidak memberi perbedaan kemampuan antar tier. Perbedaan charge kuota
  (jika ada) di luar cakupan.