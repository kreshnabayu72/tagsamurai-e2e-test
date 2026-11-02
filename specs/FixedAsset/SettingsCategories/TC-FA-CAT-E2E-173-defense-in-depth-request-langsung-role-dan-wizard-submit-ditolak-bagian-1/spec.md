---
id: TC-FA-CAT-E2E-173-defense-in-depth-request-langsung-role-dan-wizard-submit-ditolak-bagian-1
title: "Defense-in-Depth: Request Langsung Create, Edit, Delete, Bulk Delete, dan Wizard Submit Ditolak Server (Bagian 1)"
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

# Defense-in-Depth: Request Langsung Create, Edit, Delete, Bulk Delete, dan Wizard Submit Ditolak Server (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Kelas harness a (defense-in-depth: request langsung ke server tanpa melalui UI). Spec mengasersi status respons dan state data; asersi absence log ada di spec 168.
- Akun login hook `before` spec ini: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Satu ganti akun UI eksplisit pada langkah 22 ke Total Control client CatPostT0 (Pre-setup #33).
- Aktor request langsung (sesi API aktor, butir "Sesi API aktor" di `suite.md`):

  | TC | Aktor | Pre-setup | Email | Password | Client |
  |---|---|---|---|---|---|
  | TC-FA-CAT-497 | Read Only | #2 | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | CatMain (#20) |
  | TC-FA-CAT-498, TC-FA-CAT-500 | Create-Only | #4 | `createOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CO_PASSWORD` | CatMain (#20) |
  | TC-FA-CAT-499 | Update-Only | #5 | `updateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_UO_PASSWORD` | CatMain (#20) |
  | TC-FA-CAT-501 | Create-Update-Delete | #7 | `createUpdateDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CUD_PASSWORD` | CatExcess (#31) |
  | TC-FA-CAT-502, TC-FA-CAT-579 | Total Control | #1 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | CatPostT0 (#33) |

- Env var `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_CO_PASSWORD`, `FA_UO_PASSWORD`, dan `FA_CUD_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data milik spec (di-seed hook `before` lewat API; dibersihkan hook `after`; kemampuan seed disediakan tim FE/BE), nama berakhiran `{runId}-173`, client CatMain:
  - `Furniture Req {runId}-173` (Code `FR173`, leaf, Description kosong) sebagai target Edit TC-FA-CAT-498.
  - `Vehicle Req {runId}-173` (Code `VR173`, leaf) sebagai target Delete TC-FA-CAT-499.
  - `Vehicle Bulk {runId}-173` (Code `VB173`, leaf) dan `Cable Bulk {runId}-173` (Code `CB173`, leaf) sebagai target Bulk Delete TC-FA-CAT-500.
  - `Bypass Cat {runId}-173` tidak di-seed; dipakai pada request Create TC-FA-CAT-497.
- Data client Pre-setup yang dibaca: CatExcess (Pre-setup #31, 9 kategori; himpunan 5 kategori usable `Electronics`, `Laptop`, `Monitor`, `Office`, `Spare Parts` menjadi payload TC-FA-CAT-501; kategori Excess `Heavy Equipment`, `Vehicle`, `Furniture`, `Old Parts`) dan CatPostT0 (Pre-setup #33, 8 kategori, cap 5, Alert Category Consolidation tampil, belum ada seleksi tersimpan). Tidak ada baris Pre-setup yang diubah (semua request ditolak).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk request langsung dengan sesi API aktor; kemampuan membaca dari server daftar kategori beserta Description, status Excess, dan seleksi tersimpan (state data, bagian 8b butir 1).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-497: Request Create oleh Read Only

1. Kirim request Create kategori `Bypass Cat {runId}-173` langsung ke server menggunakan sesi API aktor Read Only (Pre-setup #2) hingga respons diterima
2. Verifikasi server menolak request dengan 403 Forbidden
3. Verifikasi data kategori client CatMain tidak berubah: daftar dari server memuat `Default Category` dan tidak memuat `Bypass Cat {runId}-173`

### TC-FA-CAT-498: Request Edit oleh Create-Only

4. Kirim request Edit Description kategori `Furniture Req {runId}-173` menjadi `Edit Bypass` langsung ke server menggunakan sesi API aktor Create-Only (Pre-setup #4) hingga respons diterima
5. Verifikasi server menolak request dengan 403 Forbidden
6. Verifikasi data kategori tidak berubah: Description `Furniture Req {runId}-173` pada server tetap kosong

### TC-FA-CAT-499: Request Delete oleh Update-Only

7. Kirim request Delete kategori `Vehicle Req {runId}-173` langsung ke server menggunakan sesi API aktor Update-Only (Pre-setup #5) hingga respons diterima
8. Verifikasi server menolak request dengan 403 Forbidden
9. Verifikasi data kategori tidak berubah: `Vehicle Req {runId}-173` masih ada pada daftar dari server

### TC-FA-CAT-500: Request Bulk Delete oleh Create-Only

10. Kirim request Bulk Delete kategori `Vehicle Bulk {runId}-173` dan `Cable Bulk {runId}-173` langsung ke server menggunakan sesi API aktor Create-Only (Pre-setup #4) hingga respons diterima
11. Verifikasi server menolak request dengan 403 Forbidden
12. Verifikasi data kategori tidak berubah: `Vehicle Bulk {runId}-173` dan `Cable Bulk {runId}-173` masih ada pada daftar dari server

### TC-FA-CAT-501: Request Wizard Submit oleh Create-Update-Delete

13. Kirim request Wizard Submit dengan 5 kategori usable (`Electronics`, `Laptop`, `Monitor`, `Office`, `Spare Parts`) langsung ke server menggunakan sesi API aktor Create-Update-Delete (Pre-setup #7, client CatExcess) hingga respons diterima
14. Verifikasi server menolak request dengan 403
15. Verifikasi tidak ada status Excess yang berubah: `Heavy Equipment`, `Vehicle`, `Furniture`, dan `Old Parts` tetap Excess serta lima kategori usable tetap usable pada data dari server

### TC-FA-CAT-502: Request Wizard Submit melebihi cap

16. Kirim request Wizard Submit dengan 6 kategori (cap 5) langsung ke server menggunakan sesi API aktor Total Control (Pre-setup #1, client CatPostT0) hingga respons diterima
17. Verifikasi server menolak request dengan 422
18. Kirim request Wizard Submit dengan 0 kategori langsung ke server menggunakan sesi API aktor Total Control (client CatPostT0) hingga respons diterima
19. Verifikasi server menolak request dengan 422
20. Verifikasi seleksi tidak disimpan: seleksi tersimpan CatPostT0 pada server tetap kosong
21. Verifikasi tidak ada perubahan status: kedelapan kategori CatPostT0 tetap berstatus semula pada data dari server

### TC-FA-CAT-579: Request Wizard Submit dengan 0 Keep usable

22. Ganti akun: logout, lalu login sebagai Total Control (Pre-setup #1) client CatPostT0 dengan `Spectra.env.FA_TC_PASSWORD`
23. Buka Fixed Asset > Settings > Categories
24. Klik `[Choose Categories]` pada Alert Category Consolidation
25. Verifikasi tombol `[Save Selection]` disabled saat tidak ada satu pun `Keep usable` dicentang
26. Kirim request Wizard Submit dengan 0 kategori Keep usable langsung ke server menggunakan sesi API aktor Total Control (client CatPostT0) hingga respons diterima
27. Verifikasi server menolak request dengan 422 (X = 0, tidak ada node penampung darurat)
28. Verifikasi seleksi tidak disimpan: seleksi tersimpan CatPostT0 pada server tetap kosong
29. Tutup popup Category Consolidation lewat `✕`
30. Verifikasi tidak ada perubahan status Excess pada node mana pun: kedelapan kategori CatPostT0 tetap berstatus semula pada data dari server

## Notes

- `K-1`: TC-FA-CAT-497 sampai TC-FA-CAT-502 dan TC-FA-CAT-579 berkelas a dengan Expected respons API; tetap di spec FE+BE walau tumpang tindih dengan `tc-settings-categories-backend.md`.
- Pembagian TC lintas spec: TC-FA-CAT-497 sampai TC-FA-CAT-502 dan TC-FA-CAT-579 juga ada di spec 168 (asersi "tidak ada baris log baru" milik spec absence, S-05); spec ini tidak mengasersi log. Klausa tanpa log pada Expected TC-FA-CAT-497 b, 498 b, 499 b, 500 b, 501, 502, dan 579 c ada di spec 168.
- Langkah penghubung (S-03): langkah 22 dan 23 (ganti akun dan buka halaman), langkah 29 (menutup popup tanpa perubahan form, tidak dirty). Pemulihan sesi ke akun default dilakukan hook `after` (S-07).
- Verifikasi data tidak berubah pada langkah 3 memuat `Default Category` sebagai pembanding (daftar tidak kosong) sebelum menyatakan `Bypass Cat {runId}-173` tidak ada (bagian 8b butir 2).
- Langkah 4, 7, 10 memakai data bersuffix milik spec sebagai target (S-06) walau TC menyebut `Furniture`, `Vehicle`, dan `Cable` Pre-setup.
- Temuan untuk QA:
  - TC-FA-CAT-501 tidak menyebut 5 kategori mana yang dikirim; spec memakai lima kategori usable CatExcess.
  - TC-FA-CAT-502 tidak menyebut kategori untuk payload 6 kategori; spec memilih dari 8 kategori CatPostT0.
  - Post Condition TC-FA-CAT-497 sampai TC-FA-CAT-500 ("tidak ada perubahan data") hanya punya satu padanan Expected; diasersi lewat pembacaan data dari server, kemampuan disediakan tim FE/BE.
  - Nama env var password aktor tidak tertulis di TC; semua nama adalah usulan.
  - TC-FA-CAT-579 Expected c mencampur klausa FE ("Alert Category Consolidation tetap tampil") dengan absence log pada request langsung. Klausa FE tidak diasersi di spec ini karena tidak menguji apa pun sesudah request langsung (bagian 8b butir 1); perlu dipisah di TC (klausa Alert ke spec jalur form, absence log ke spec 168).
