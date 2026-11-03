---
id: TC-FA-CAT-E2E-168-absence-log-request-langsung-ditolak-changelog-system-log-activity-log
title: "Absence Log: Request Langsung yang Ditolak Server Tidak Menulis Baris Changelog, System Log, dan Activity Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-497
  - TC-FA-CAT-498
  - TC-FA-CAT-499
  - TC-FA-CAT-500
  - TC-FA-CAT-501
  - TC-FA-CAT-502
  - TC-FA-CAT-579
coverage:
  web: automated
---

# Absence Log: Request Langsung yang Ditolak Server Tidak Menulis Baris Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Kelas harness g (asersi absence). Pemicu kelas a (request langsung ke server) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (`P-5` butir a). Spec tidak mengasersi tampilan UI; tidak ada langkah UI di `## Test Steps`.
- Akun login hook `before` spec ini: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun UI di tengah spec.
- Aktor request langsung (sesi API aktor, butir "Sesi API aktor" di `suite.md`; login API memakai password dan token tidak dihitung sebagai sesi web):

  | TC | Aktor | Pre-setup | Email | Password | Client |
  |---|---|---|---|---|---|
  | TC-FA-CAT-497 | Read Only | #2 | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | CatMain (#20) |
  | TC-FA-CAT-498, TC-FA-CAT-500 | Create-Only | #4 | `createOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CO_PASSWORD` | CatMain (#20) |
  | TC-FA-CAT-499 | Update-Only | #5 | `updateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_UO_PASSWORD` | CatMain (#20) |
  | TC-FA-CAT-501 | Create-Update-Delete | #7 | `createUpdateDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CUD_PASSWORD` | CatExcess (#31) |
  | TC-FA-CAT-502, TC-FA-CAT-579 | Total Control | #1 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | CatPostT0 (#33) |

- Env var `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_CO_PASSWORD`, `FA_UO_PASSWORD`, dan `FA_CUD_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data milik spec (di-seed hook `before` lewat API; dibersihkan hook `after`; kemampuan seed disediakan tim FE/BE), nama berakhiran `{runId}-168`, client CatMain:
  - `Furniture Req {runId}-168` (Code `FR168`, leaf) sebagai target Edit TC-FA-CAT-498.
  - `Vehicle Req {runId}-168` (Code `VR168`, leaf) sebagai target Delete TC-FA-CAT-499.
  - `Vehicle Bulk {runId}-168` (Code `VB168`, leaf) dan `Cable Bulk {runId}-168` (Code `CB168`, leaf) sebagai target Bulk Delete TC-FA-CAT-500.
  - `Bypass Cat {runId}-168` tidak di-seed; dipakai sebagai nama pada request Create TC-FA-CAT-497.
- Data client Pre-setup yang dibaca: CatExcess (Pre-setup #31, 9 kategori; himpunan 5 kategori usable `Electronics`, `Laptop`, `Monitor`, `Office`, `Spare Parts` dipakai sebagai payload TC-FA-CAT-501) dan CatPostT0 (Pre-setup #33, 8 kategori, cap 5, belum ada seleksi tersimpan; payload TC-FA-CAT-502 dan TC-FA-CAT-579). Tidak ada baris Pre-setup yang diubah (request ditolak).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk request langsung dengan sesi API aktor; kemampuan membaca jumlah entri Modal Changelog, System Log, dan Activity Log milik client yang bersangkutan sebelum dan sesudah aksi (bagian 8b butir 10: total audit trail tidak diturunkan dari seeding, asersi memakai selisih terhadap baseline, S-12).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-497: Request Create oleh Read Only

1. Catat baseline jumlah entri Modal Changelog, System Log, dan Activity Log client CatMain
2. Kirim request Create kategori `Bypass Cat {runId}-168` langsung ke server menggunakan sesi API aktor Read Only (Pre-setup #2) hingga respons diterima
3. Verifikasi server menolak request dengan 403 Forbidden
4. Verifikasi jumlah entri Modal Changelog, System Log, dan Activity Log client CatMain sama dengan baseline (tidak ada baris log baru)

### TC-FA-CAT-498: Request Edit oleh Create-Only

5. Catat baseline jumlah entri Modal Changelog, System Log, dan Activity Log client CatMain
6. Kirim request Edit Description kategori `Furniture Req {runId}-168` langsung ke server menggunakan sesi API aktor Create-Only (Pre-setup #4) hingga respons diterima
7. Verifikasi server menolak request dengan 403 Forbidden
8. Verifikasi jumlah entri Modal Changelog, System Log, dan Activity Log client CatMain sama dengan baseline (tidak ada baris log baru)

### TC-FA-CAT-499: Request Delete oleh Update-Only

9. Catat baseline jumlah entri Modal Changelog, System Log, dan Activity Log client CatMain
10. Kirim request Delete kategori `Vehicle Req {runId}-168` langsung ke server menggunakan sesi API aktor Update-Only (Pre-setup #5) hingga respons diterima
11. Verifikasi server menolak request dengan 403 Forbidden
12. Verifikasi jumlah entri Modal Changelog, System Log, dan Activity Log client CatMain sama dengan baseline (tidak ada baris log baru)

### TC-FA-CAT-500: Request Bulk Delete oleh Create-Only

13. Catat baseline jumlah entri Modal Changelog, System Log, dan Activity Log client CatMain
14. Kirim request Bulk Delete kategori `Vehicle Bulk {runId}-168` dan `Cable Bulk {runId}-168` langsung ke server menggunakan sesi API aktor Create-Only (Pre-setup #4) hingga respons diterima
15. Verifikasi server menolak request dengan 403 Forbidden
16. Verifikasi jumlah entri Modal Changelog, System Log, dan Activity Log client CatMain sama dengan baseline (tidak ada baris log baru)

### TC-FA-CAT-501: Request Wizard Submit oleh Create-Update-Delete

17. Catat baseline jumlah entri Modal Changelog, System Log, dan Activity Log client CatExcess
18. Kirim request Wizard Submit dengan 5 kategori usable (`Electronics`, `Laptop`, `Monitor`, `Office`, `Spare Parts`) langsung ke server menggunakan sesi API aktor Create-Update-Delete (Pre-setup #7, client CatExcess) hingga respons diterima
19. Verifikasi server menolak request dengan 403
20. Verifikasi jumlah entri Modal Changelog, System Log, dan Activity Log client CatExcess sama dengan baseline (tidak ada baris log)

### TC-FA-CAT-502: Request Wizard Submit melebihi cap

21. Catat baseline jumlah entri Modal Changelog, System Log, dan Activity Log client CatPostT0
22. Kirim request Wizard Submit dengan 6 kategori (cap 5) langsung ke server menggunakan sesi API aktor Total Control (Pre-setup #1, client CatPostT0) hingga respons diterima
23. Verifikasi server menolak request dengan 422
24. Kirim request Wizard Submit dengan 0 kategori langsung ke server menggunakan sesi API aktor Total Control (client CatPostT0) hingga respons diterima
25. Verifikasi server menolak request dengan 422
26. Verifikasi jumlah entri Modal Changelog, System Log, dan Activity Log client CatPostT0 sama dengan baseline (tidak ada log)

### TC-FA-CAT-579: Request Wizard Submit dengan 0 Keep usable

27. Catat baseline jumlah entri Modal Changelog client CatPostT0
28. Kirim request Wizard Submit dengan 0 kategori Keep usable langsung ke server menggunakan sesi API aktor Total Control (client CatPostT0) hingga respons diterima
29. Verifikasi server menolak request dengan 422
30. Verifikasi jumlah entri Modal Changelog client CatPostT0 sama dengan baseline (tidak ada baris Changelog baru)

## Notes

- `K-1`: TC-FA-CAT-497 sampai TC-FA-CAT-502 dan TC-FA-CAT-579 berkelas a dengan Expected respons API; tetap di spec FE+BE walau tumpang tindih dengan `tc-settings-categories-backend.md`.
- `P-5` (butir a): spec absence ini memuat request langsung kelas a sebagai pemicu. Tiap TC punya aktor, client, dan baseline sendiri (langkah 1, 5, 9, 13, 17, 21, 27).
- Pembagian TC lintas spec: TC-FA-CAT-497 sampai TC-FA-CAT-502 dan TC-FA-CAT-579 juga ada di spec 173; spec 173 mengasersi status respons dan state data (bagian 8b butir 1, S-05), spec ini mengasersi absence log. TC-FA-CAT-579 juga punya asersi UI (tombol `[Save Selection]` disabled, Alert Category Consolidation tetap tampil) di spec 173.
- Anchor positif absence (bagian 8b butir 2): respons penolakan (403 atau 422) pada langkah 3, 7, 11, 15, 19, 23, 25, 29 membuktikan request diproses server, dan baseline jumlah entri pada langkah baseline menjadi pembanding surface agregat. Asersi memakai selisih jumlah entri terhadap baseline (S-12), bukan angka absolut.
- Langkah 2, 6, 10, 14 memakai data bersuffix milik spec sebagai target request (S-06) walau TC menyebut `Furniture`, `Vehicle`, dan `Cable` Pre-setup.
- Temuan untuk QA:
  - TC-FA-CAT-497 sampai TC-FA-CAT-502 menulis "tidak ada baris log baru" tanpa menyebut surface; spec memeriksa Modal Changelog, System Log, dan Activity Log (tiga surface pencatatan modul menurut TC-FA-CAT-580). TC-FA-CAT-579 hanya menyebut Changelog dan diperiksa pada surface itu saja.
  - TC-FA-CAT-501 tidak menyebut 5 kategori mana yang dikirim; spec memakai lima kategori usable CatExcess.
  - TC-FA-CAT-502 tidak menyebut kategori untuk payload 6 kategori; spec memilih dari 8 kategori CatPostT0.
  - Nama env var password aktor tidak tertulis di TC; semua nama adalah usulan.
  - Lokasi System Log dan Activity Log tidak disebut TC; kemampuan baca disediakan tim FE/BE.
