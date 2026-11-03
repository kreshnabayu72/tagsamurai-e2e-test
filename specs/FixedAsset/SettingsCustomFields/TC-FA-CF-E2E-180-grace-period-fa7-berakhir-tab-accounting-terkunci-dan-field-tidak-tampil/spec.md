---
id: TC-FA-CF-E2E-180-grace-period-fa7-berakhir-tab-accounting-terkunci-dan-field-tidak-tampil
title: "Grace Period FA-7 Berakhir: Tab Accounting Terkunci dan Field Accounting Tidak Tampil"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-670
coverage:
  web: automated
---

# Grace Period FA-7 Berakhir: Tab Accounting Terkunci dan Field Accounting Tidak Tampil

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Grace (Pre-setup #25). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_GRACE_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Grace (Pre-setup #25): FA-7 sempat aktif lalu diturunkan ke None efektif T-0 dengan Grace Period berjalan (T+10 hari), dipulihkan hook `before` lewat seed reset Company Grace; field Accounting `Cost Center` bernilai pada aset `A1`; field General `Asset Serial Tag` Active bernilai pada `A1` dan `A2`. Nilai data mengacu `Fixture.faCustomFields.grace` (fixture belum ada, disediakan tim FE).
- Waktu: waktu seed dimajukan melewati T+30 hari (T+31 hari) pada langkah 1 lewat seed Company Grace (disediakan tim FE/BE). Jam server dan jam browser tidak diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: waktu seed Company Grace dimajukan pada langkah 1; hook `after` memulihkan waktu seed dan Grace Period berjalan lewat seed reset Company Grace. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-670: Grace Period berakhir

1. Majukan waktu seed Company Grace hingga T+31 hari sehingga Grace Period berakhir
2. Muat ulang Settings > Custom Fields
3. Arahkan kursor ke tab `Accounting`
4. Verifikasi tab `Accounting` disabled dengan icon 🔒
5. Verifikasi tooltip `Accounting fields require the Accounting & Depreciation feature. Upgrade your plan to unlock them.` tampil
6. Klik tab `Accounting`
7. Verifikasi klik tab `Accounting` tidak membuka tabel Accounting
8. Buka Detail aset `A1`
9. Verifikasi Detail aset `A1` tampil
10. Verifikasi `Cost Center` tidak tampil di Detail aset `A1`
11. Buka Asset List dan buka daftar Column Visibility
12. Verifikasi `Asset Serial Tag` tersedia sebagai kolom opsional di Asset List
13. Verifikasi `Cost Center` tidak tersedia sebagai kolom opsional di Asset List

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Satu subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (memajukan waktu seed, pemicu state kelas h), langkah 2 (memuat ulang halaman setelah state berubah). Langkah 9 dan 12 adalah anchor positif untuk asersi absence `Cost Center` di Detail dan Column Visibility (bagian 8b butir 2).
- TC-FA-CF-670 ada di spec ini; TC lain Grace Period ada di spec 145 dan 146.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Grace; akun disediakan tim FE.
  - TC-FA-CF-670 tidak menyebut kapan Grace Period dianggap berakhir selain "T+31 hari"; spec memajukan waktu seed melewati T+30 hari sesuai Pre-setup #24 dan #25.
