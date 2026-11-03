---
id: TC-AC-DS-E2E-118-changelog-filter-logika-or-and-dan-chip
title: "Filter Changelog: Logika OR dan AND serta Penghapusan Chip dan Un-check Opsi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-401
  - TC-AC-DS-402
  - TC-AC-DS-403
coverage:
  web: automated
---

# Filter Changelog: Logika OR dan AND serta Penghapusan Chip dan Un-check Opsi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): 35 entri, termasuk Create `BLE-KIN-GW1` dan Delete `HHR-ARC-300`, keduanya oleh `Jane S`. Keadaan awal 35 entri dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; filter dilepas oleh langkah pemulihan setiap bagian.

## Test Steps

### TC-AC-DS-401: Logika OR dan AND

1. Klik ikon Changelog
2. Klik ikon Filter pada modal
3. Pada field Action pilih `Create` dan `Delete`
4. Klik `[Apply]` pada Filter Panel modal
5. Verifikasi tabel memuat entri Create `BLE-KIN-GW1` dan Delete `HHR-ARC-300`
6. Tambahkan filter Modified By `Jane S`, lalu klik `[Apply]`
7. Verifikasi kedua entri tetap tampil karena keduanya oleh `Jane S`
8. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-402: Hapus chip lewat ikon silang

9. Pada field Action pilih `Create` dan `Delete`
10. Klik ikon `(✕)` pada chip `Create`
11. Verifikasi chip `Create` hilang
12. Verifikasi chip `Delete` tetap ada
13. Buka dropdown Action
14. Verifikasi checkbox `Create` tidak tercentang di dalam dropdown
15. Tekan Esc, lalu klik `[Apply]` pada Filter Panel modal
16. Verifikasi tabel hanya memuat entri Delete `HHR-ARC-300`
17. Klik `[Clear Field]`, lalu `[Apply]`

### TC-AC-DS-403: Un-check opsi di dalam dropdown

18. Pada field Action pilih `Create` dan `Delete`
19. Buka dropdown Action lalu hilangkan centang `Create`
20. Verifikasi chip `Create` hilang dari field
21. Verifikasi chip `Delete` tetap ada
22. Tekan Esc, lalu klik `[Apply]` pada Filter Panel modal
23. Verifikasi tabel hanya memuat entri Delete `HHR-ARC-300`
24. Klik `[Clear Field]`, lalu `[Apply]`
25. Klik ikon close `[✕]` pada modal

## Notes

- Langkah penghubung (S-03, S-09): `[Clear Field]` lalu `[Apply]` di langkah 8, 17, dan 24 melepas filter; Esc di langkah 15 dan 22 menutup dropdown sebelum `[Apply]`; langkah 25 menutup modal; tanpa asersi tambahan.
- Asersi "hanya" pada langkah 16 dan 23 memakai entri Delete `HHR-ARC-300` yang dijamin tampil oleh filter sebagai pembanding.
- Temuan untuk QA:
  - S-12: Pre-setup #33 menetapkan keadaan awal entri (Create `BLE-KIN-GW1` dan Delete `HHR-ARC-300` saja pada Action `Create` dan `Delete`); konvensi menyatakan audit trail tumbuh sehingga asersi bergantung pada baseline data uji. Spec mengikuti TC; keputusan pengecualian masih terbuka. Asersi juga bergantung pada nama literal Pre-setup #29 dan #30; Lampiran A tidak memuat butir modul ini.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
