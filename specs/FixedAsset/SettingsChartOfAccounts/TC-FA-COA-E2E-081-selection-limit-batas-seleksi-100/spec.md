---
id: TC-FA-COA-E2E-081-selection-limit-batas-seleksi-100
title: "Selection Limit: Batas Seleksi 100 pada Select All, Seleksi Manual, dan Permintaan Langsung Bulk"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-140
  - TC-FA-COA-141
  - TC-FA-COA-276
coverage:
  web: automated
---

# Selection Limit: Batas Seleksi 100 pada Select All, Seleksi Manual, dan Permintaan Langsung Bulk

## Prerequisites

- Mode: FE+BE.
- Kelas harness e (volume data: Selection Limit 100 dengan 101 akun). Suite berjalan serial (`parallel: false`).
- Akun login hook `before` spec ini: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada client uji Selection Limit (Pre-setup P26), password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` sudah terdaftar. Kecocokan akun Total Control pada client P26 perlu dikonfirmasi tim FE.
- Data Pre-setup: client P26 dengan Selection Limit 100 (nilai minimum, Lifecycle Settings > System Limits) dan 101 akun Active, disiapkan tim FE lewat seed atau API (kunci fixture ditetapkan tim FE). Tidak ada akun yang diubah; semua aksi seleksi dibatalkan atau ditolak.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): sesi API aktor Total Control (butir "Sesi API aktor" di `suite.md`); klien HTTP untuk permintaan langsung; kemampuan membaca dari server jumlah akun Active client P26.
- Seed dan pemulihan client mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.

## Test Steps

### TC-FA-COA-140: Select All melebihi Selection Limit

1. Centang checkbox header tabel
2. Klik `Select All (101 records)`
3. Verifikasi seleksi dibatasi ke 100 baris pertama: counter `100 Accounts selected`
4. Verifikasi Bulk Action Bar tampil dengan aksi `Deactivate` dan `Delete` aktif
5. Verifikasi Toast error "Error, only the first 100 of 101 rows were selected. Narrow your filter to include the rest." tampil dan persisten sampai di-dismiss
6. Verifikasi button `Select All (101 records)` tetap tampil
7. Dismiss Toast error
8. Klik ikon `(X)` pada Bulk Action Bar

### TC-FA-COA-141: Seleksi manual hingga batas

9. Atur ukuran halaman tabel menjadi 100
10. Klik checkbox header di halaman 1 sehingga 100 baris tercentang
11. Pindah ke halaman 2
12. Arahkan kursor ke checkbox baris ke-101
13. Verifikasi checkbox baris ke-101 Disabled dengan tooltip "You've reached the maximum selection of 100 rows."
14. Coba centang checkbox baris ke-101
15. Verifikasi checkbox baris ke-101 tidak dapat dicentang
16. Kembali ke halaman 1
17. Verifikasi 100 baris di halaman 1 tetap tercentang
18. Verifikasi Bulk Action Bar tampil dengan aksi `Deactivate` dan `Delete` aktif
19. Klik ikon `(X)` pada Bulk Action Bar

### TC-FA-COA-276: Permintaan langsung Bulk Deactivate melebihi batas

20. Catat jumlah akun Active client P26 dari server (baseline, 101)
21. Kirim permintaan langsung Bulk Deactivate untuk 101 akun sekaligus ke server menggunakan sesi API aktor Total Control hingga respons diterima
22. Verifikasi permintaan ditolak server sebelum diproses
23. Verifikasi tidak ada akun yang berubah status: jumlah akun Active client P26 dari server sama dengan langkah 20

## Notes

- `K-1`: TC-FA-COA-276 berkelas a dengan Expected respons API dan state data; tetap di spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Alasan 23 langkah: tidak ada; di bawah ambang sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 1 (memunculkan `Select All (101 records)` lewat centang header), langkah 7 dan 8 (dismiss toast dan pemulihan seleksi), langkah 9 (ukuran halaman 100 sesuai Precondition TC-FA-COA-141), langkah 19 (pemulihan seleksi), langkah 20 (baseline). Ukuran halaman tidak dipulihkan karena spec berikutnya mengatur sendiri tabelnya (perlu dikonfirmasi tim FE bila preferensi ukuran halaman bertahan lintas sesi).
- Penolakan permintaan langsung pada langkah 22 hanya mengasersi respons server dan state data (bagian 8b butir 1); asersi "tidak ada entri log" tidak ada di spec ini.
- Temuan untuk QA:
  - TC-FA-COA-140 tidak menyebut bagaimana tombol `Select All (101 records)` muncul (centang header) dan ukuran halamannya; Precondition menyebut "101 akun yang cocok dengan filter aktif" tanpa menyebut filter. Spec tidak menerapkan filter.
  - TC-FA-COA-140 menyebut `Select All (101 records)` tetap tampil, tetapi tidak menyebut label counter; spec memakai `100 Accounts selected` mengikuti pola counter `N Accounts selected` pada TC lain.
  - TC-FA-COA-140 dan TC-FA-COA-276 Post Condition ("tidak ada perubahan data", "tidak ada entri log") tanpa langkah observasi pada TC-FA-COA-140 dan 276 (kecuali langkah 23 untuk status akun); log tidak diasersi.
  - TC-FA-COA-276 tidak menyebut status respons (kode); spec hanya mengasersi "ditolak".
