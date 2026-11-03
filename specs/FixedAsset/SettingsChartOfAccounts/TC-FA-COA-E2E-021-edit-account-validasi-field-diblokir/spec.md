---
id: TC-FA-COA-E2E-021-edit-account-validasi-field-diblokir
title: "Edit Account: Validasi Field Diblokir"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-253
  - TC-FA-COA-254
  - TC-FA-COA-255
  - TC-FA-COA-256
  - TC-FA-COA-257
  - TC-FA-COA-258
coverage:
  web: automated
---

# Edit Account: Validasi Field Diblokir

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin`, Function Depreciation Expense | Active, Used By 0, belum pernah diekspor; hanya dibaca (semua kasus diblokir sebelum tersimpan) | TC-253 sampai TC-258 |

- Data uji validasi (literal dari kolom Data TC, tidak dibuat ke server):

  | Kasus | Nilai |
  |---|---|
  | Account Code 15 karakter | `ABCDEFGHIJKLMNO` |
  | Account Code 16 karakter | `ABCDEFGHIJKLMNOP` |
  | Account Code di luar whitelist | `1/1001` |
  | Account Name 120 karakter | 120 karakter `A` |
  | Account Name 121 karakter | 121 karakter `A` |
  | Account Name berisi emoji | `Fixed Assets 🚗` |

- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Buka form Edit P1

1. Ketik Search `5-6001`, tekan Enter
2. Klik row action `Edit` pada akun P1 (`5-6001`)

### TC-FA-COA-253: Account Code dikosongkan memunculkan caption wajib diisi (V-01)

3. Kosongkan Account Code
4. Klik `[Save]`
5. Verifikasi caption "Account code must not be empty" di field Account Code
6. Verifikasi modal Edit Account tetap terbuka

### TC-FA-COA-254: Batas panjang Account Code 15 karakter diterima, 16 karakter ditolak (V-02)

7. Ketik 15 karakter `ABCDEFGHIJKLMNO` di Account Code
8. Verifikasi field Account Code berisi `ABCDEFGHIJKLMNO`
9. Verifikasi tidak ada caption pada field Account Code
10. Tambah satu karakter `P` di Account Code
11. Verifikasi caption "Max. 15 characters" muncul langsung saat mengetik

### TC-FA-COA-255: Karakter Account Code di luar whitelist ditolak (V-03)

12. Ganti isi Account Code dengan `1/1001`
13. Verifikasi caption "Account code contains invalid characters" muncul langsung saat mengetik

### TC-FA-COA-256: Batas panjang Account Name 120 karakter diterima, 121 karakter ditolak (V-06)

14. Ganti isi Account Code dengan `5-6001`
15. Ganti isi Account Name dengan 120 karakter `A`
16. Verifikasi field Account Name berisi 120 karakter `A`
17. Verifikasi tidak ada caption pada field Account Name
18. Tambah satu karakter `A` di Account Name
19. Verifikasi caption "Max. 120 characters" muncul langsung saat mengetik

### TC-FA-COA-257: Account Name berisi emoji diblokir di input (V-07)

20. Ganti isi Account Name dengan `Fixed Assets 🚗`
21. Verifikasi karakter emoji tidak masuk ke input Account Name

### TC-FA-COA-258: Account Function dikosongkan lewat `[Clear Field]` memunculkan caption wajib dipilih (V-08)

22. Klik `[Clear Field]`
23. Isi Account Code `5-6001`
24. Isi Account Name `Depreciation Expense – Admin`
25. Klik `[Save]`
26. Verifikasi caption "Account function must not be empty" di field Account Function
27. Verifikasi modal Edit Account tetap terbuka

### Tutup form dan pastikan tidak ada yang tersimpan

28. Klik `[✕]` di header modal
29. Verifikasi dialog Unsaved Changes tampil
30. Klik `[Leave]`
31. Verifikasi baris P1 pada tabel tetap menampilkan Account Code `5-6001` dan Account Name `Depreciation Expense – Admin` sehingga tidak ada perubahan tersimpan pada kasus TC-253 dan TC-258

## Notes

- Satu pembukaan form Edit dipakai untuk seluruh kasus diblokir (prinsip 13, halaman yang sama dipakai berulang); form ditutup deterministik di akhir (langkah 28 sampai 30, S-08).
- Langkah penghubung (S-03, R-12, R-16): Search Account Code membuka baris target (langkah 1); langkah 14 mengembalikan Account Code ke nilai valid dan langkah 12 sampai 15 mengganti isi field sehingga caption kasus sebelumnya tidak terbawa; langkah 8, 16 membuktikan isi field sebagai anchor positif sebelum asersi absence caption (langkah 9, 17, 8b.2).
- Panjang 120 dan 121 karakter pada langkah 15 dan 18 dihitung langsung tanpa suffix `{runId}`; Account Name pada kasus ini tidak disimpan ke server.
- Asersi "tidak ada perubahan tersimpan" TC-253 dan TC-258 dibaca dari baris P1 sesudah modal ditutup lewat `[Leave]` (langkah 31), karena TC tidak memberi cara cek lain.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-257 butir b ("Bila lolos sampai submit, muncul 'Account name contains invalid characters'") bersyarat dan tidak dapat diasersi deterministik bila butir a terpenuhi (emoji tidak masuk ke input); spec hanya mengasersi butir a (langkah 21) dan tidak menulis langkah bersyarat.
  - Data "Account Name 120 karakter" tidak menyebut karakter yang dipakai; spec memakai karakter `A` (konsisten dengan D13 di TC).
