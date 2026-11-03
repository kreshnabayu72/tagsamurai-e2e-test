---
id: TC-FA-COA-E2E-016-add-account-validasi-duplikat-code-dan-create-dengan-search-dan-filter
title: "Add Account: Validasi Duplikat Code dan Create dengan Search dan Filter Aktif"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-28
  - TC-FA-COA-29
  - TC-FA-COA-143
coverage:
  web: automated
---

# Add Account: Validasi Duplikat Code dan Create dengan Search dan Filter Aktif

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P2 | `6-2001 – Repairs & Maintenance Expense` | Function Capitalization Offset, Active; hanya dibaca | TC-29 |
  | P5 | `CAP-6100 – Capitalization Clearing – Repairs` | Function Capitalization Offset, Active; hanya dibaca | TC-28 (diketik `cap-6100` huruf kecil) |

- Tabel berisi lebih dari 10 akun dengan ukuran halaman 10 (disediakan tim FE lewat seed Pre-setup).
- Data Dinamis (D3, dibuat spec lewat UI): Account Code `5-6150`, Account Name `Depreciation Expense – Branch Surabaya {runId}-016`, Function Depreciation Expense; tetap Active. Account Code maksimal 15 karakter sehingga tidak memuat `{runId}`; identitas run dibawa Account Name. Name pemeriksa penolakan TC-28 dan TC-29: `Duplicate Code Test {runId}-016` (tidak boleh tersimpan).
- Pembersihan: hook `before` dan `after` spec ini menghapus akun dengan Account Code `5-6150` bila ada (dan akun dengan Name `Duplicate Code Test {runId}-016` bila ada); kemampuan hapus lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Pembukaan form

1. Klik `+ Account` di toolbar

### TC-FA-COA-28: Account Code duplikat case-insensitive (V-04)

2. Ketik `cap-6100` di Account Code
3. Tunggu sekitar 500 ms (debounce)
4. Verifikasi caption "Account code already exists" muncul setelah debounce
5. Isi Account Name `Duplicate Code Test {runId}-016` dan pilih Account Function Capitalization Offset
6. Klik `[Submit]`
7. Verifikasi modal Add Account tetap terbuka

### TC-FA-COA-29: Account Code `6-2001` yang sudah ada ditolak

8. Klik `[Clear Field]`
9. Isi Account Code `6-2001`, Account Name `Duplicate Code Test {runId}-016`, dan pilih Account Function Capitalization Offset
10. Klik `[Submit]`
11. Verifikasi caption "Account code already exists"

### Pembacaan akhir tabel (TC-28 butir b, TC-29 butir b)

12. Klik `[✕]` di header modal
13. Verifikasi dialog Unsaved Changes tampil
14. Klik `[Leave]`
15. Ketik Search `Duplicate Code Test {runId}-016`, tekan Enter
16. Verifikasi akun baru tidak dibuat: tabel menampilkan "No results found"
17. Ganti isi kotak search dengan `6-2001`, tekan Enter
18. Verifikasi hanya ada satu baris dengan Account Code `6-2001` (akun baru tidak dibuat)
19. Verifikasi akun P2 tidak berubah: Account Name `Repairs & Maintenance Expense`, Function Capitalization Offset, Status Active
20. Klik `(←)` pada kotak Search

### TC-FA-COA-143: Create saat Search dan Filter Panel aktif

21. Ketik Search `Depreciation`, tekan Enter
22. Buka Filter Panel, pilih Active = Inactive, klik `[Apply]`
23. Klik header Account Name satu kali
24. Klik `+ Account` di toolbar
25. Isi Account Code `5-6150`, Account Name `Depreciation Expense – Branch Surabaya {runId}-016`, dan pilih Account Function Depreciation Expense
26. Klik `[Submit]`
27. Verifikasi toast "Success, account has been created."
28. Verifikasi modal Add Account tertutup (checkbox "Stay on this form after submitting" tidak tercentang)
29. Verifikasi baris `5-6150` di-highlight
30. Verifikasi tabel menampilkan halaman yang memuat `5-6150`
31. Verifikasi tabel kembali ke sort default Account Code A-Z
32. Verifikasi ukuran halaman tabel 10
33. Verifikasi kotak Search kosong
34. Verifikasi chip filter aktif dan `Clear all` tidak tampil
35. Verifikasi highlight pada baris `5-6150` hilang tanpa interaksi pengguna

## Notes

- Spec ini 35 langkah. TC-143 saja memuat lima butir Expected yang, dipecah satu `Verifikasi` per klausa (S-01), menjadi sembilan `Verifikasi` (langkah 27 sampai 35); TC-28 dan TC-29 memakai satu pembukaan modal.
- Langkah penghubung (S-03): langkah 3 (jeda debounce 500 ms dari TC-28), langkah 8 (`[Clear Field]`), langkah 12 sampai 14 (tutup form dirty deterministik, S-08), langkah 15, 17, 21 (Search, R-16), langkah 20 (kosongkan Search, S-09).
- Pembacaan "akun baru tidak dibuat" TC-28 (b) dan TC-29 (b) dilakukan pada langkah 16 dan 18 setelah modal ditutup; empty state hasil Search menjadi anchor absence yang sah (8b butir 2). Langkah 19 membaca "akun P2 tidak berubah" (TC-29 b).
- Urutan langkah 29 dan 35 mengikuti urutan state (highlight sementara diasersi sebelum asersi lain, 8b butir 5), bukan urutan penulisan Expected TC-143.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-28 Expected (b) "Tombol `[Submit]` tidak membuat akun" tidak punya langkah Submit di Langkah Uji TC; spec menambah pengisian Account Name, Function, dan klik `[Submit]` (langkah 5 dan 6) agar Expected dapat diuji.
  - TC-143 tidak menyebut apakah hasil Search `Depreciation` dengan Active = Inactive memuat baris; spec tidak mengasersi isi tabel sebelum Create.
  - Account Code `5-6150` literal tanpa suffix `{runId}` karena batas 15 karakter; pembersihan hook memakai Code literal itu (R-13). Post Condition TC-143 (log L-01 di tiga surface) tidak punya langkah observasi di TC sehingga tidak diasersi.
