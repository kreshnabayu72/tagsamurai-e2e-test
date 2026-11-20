---
id: TC-FA-FAAC-E2E-203-edit-versi-scheduled-tax-method-memakai-irisan-yang-sama
title: "Edit Asset Class: Versi Scheduled Memakai Irisan Tax Method yang Sama"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-745
sourceRules: ["F-FAAC-02.k21", "E-FAAC-123", "FAAC-LOGIC-02l", "FAAC-LOGIC-07d", "ST-38"]
smoke: []
dependsOn: []
trace:
  "ST-38": 6
  "FAAC-LOGIC-02l": [6, 7]
  "F-FAAC-02.k21": [6, 7]
  "E-FAAC-123": 6
  "FAAC-LOGIC-07d": [14, 15, 17]
coverage:
  web: automated
---

# Edit Asset Class: Versi Scheduled Memakai Irisan Tax Method yang Sama

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke nilai awal oleh fixture BE di hook `before` dan `after`): Asset Class `B-IRISAN` (dipakai aset: 1 Asset Name dengan 3 aset aktif, Method `Straight Line`, Useful Life 60, Tax Depreciation Class `Seed Irisan A` dengan Tax Method `Straight Line`, tanpa versi Scheduled); `Seed Irisan A` (Active; versi Current mengizinkan `Straight Line` dan `Declining Balance`; satu versi Scheduled sejak M+2 hanya mengizinkan `Straight Line`). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Jam: M = bulan berjalan menurut zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser spec ini. Bulan pada Effective From dan tooltip ditulis format `MMM yyyy`; asersi memakai M+n relatif terhadap M. Effective From yang dipilih adalah M+1.
- Data Dinamis: tidak ada. Spec mengubah Useful Life `B-IRISAN` dari 60 menjadi 72 sebagai versi Scheduled M+1; nilai dipulihkan fixture BE.
- Kemampuan teknis (disediakan tim FE/BE): hover pada opsi select (langkah 5); fixture BE untuk seed dan pemulihan `B-IRISAN` (versi Scheduled M+1 dihapus dan Useful Life berlaku tetap 60).
- State global: versi Scheduled M+1 pada `B-IRISAN` dihapus oleh fixture BE di hook `after`; entri Changelog yang tercatat adalah audit trail permanen dan tidak diasersi.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps
1. Ketik Search `B-IRISAN`, tekan Enter
2. Klik link Class Code `B-IRISAN` di tabel
3. Klik tab `Depreciation`
4. Buka select Tax Method
5. Arahkan kursor ke opsi `Declining Balance`
6. Verifikasi opsi `Declining Balance` Disabled dengan tooltip `Not allowed from <M+2 dalam format MMM yyyy>.`
7. Verifikasi opsi `Straight Line` Enabled
8. Tutup select Tax Method tanpa mengubah pilihan (Tax Method tetap `Straight Line`)
9. Ubah Useful Life dari 60 menjadi 72
10. Klik `Save`
11. Pilih Effective From satu bulan sesudah bulan berjalan (M+1)
12. Klik `Apply`
13. Verifikasi halaman tetap di Detail mode Edit
14. Verifikasi toast sukses tampil di halaman Detail: `Success, asset class has been updated.`
15. Verifikasi Alert info `Next version starts <M+1 dalam format MMM yyyy>.` tampil di atas bar tab
16. Klik tab `Depreciation`
17. Verifikasi tab Depreciation (versi terakhir) menampilkan Useful Life 72
18. Verifikasi tab Depreciation (versi terakhir) menampilkan Tax Method `Straight Line`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-745). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16 dan bagian 8b butir 13), langkah 8 (menutup select tanpa mengubah pilihan, sesuai langkah TC "Tutup select dengan Tax Method tetap Straight Line"), dan langkah 11 (memilih Effective From pada dialog Apply Changes).
- Langkah 6 dan 7 diasersi saat select terbuka, sebelum ditutup (bagian 8b butir 5).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-IRISAN` adalah seed bertanda `B-*` per TC, dipakai apa adanya; pemulihan oleh fixture BE.
- Temuan untuk QA: TC-745 tidak menyebut kotak dialog tempat Effective From dipilih; spec mengikuti alur Save lalu Apply seperti spec versi Scheduled lain.
