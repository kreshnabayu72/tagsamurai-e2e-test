---
id: TC-GS-NLU-E2E-088-list-pagination-kolom-curated-last-update-hasil-import-dan
title: "List Pagination, kolom curated, nama panjang, Last Update hasil Import, dan hapus baris terakhir di halaman terakhir"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-305
  - TC-GS-NLU-306
  - TC-GS-NLU-308
  - TC-GS-NLU-453
  - TC-GS-NLU-483
  - TC-GS-NLU-307
coverage:
  web: automated
---

# List Pagination, kolom curated, nama panjang, Last Update hasil Import, dan hapus baris terakhir di halaman terakhir

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 13 dan 16; hanya dibaca, tidak diubah, tanpa suffix): seluruh Non-Login User Pre-setup (lebih dari 10 baris, populasi precondition TC-GS-NLU-305 dan TC-GS-NLU-306); `Rina Marlina` (Temporary User, Temporary Until hari seeding + 30 hari, Blood Type `O`); `Siti Rahayu` (bukan Temporary User); Non-Login User `Nama Panjang` (First Name 60 karakter dan Last Name 60 karakter; kata kunci Search `Fixture.nonLoginUser.namaPanjang.kunciSearch`, fixture baru); General Settings Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Pre-setup No. 16). Fixture baru `Fixture.nonLoginUser.preSetup` di `fixtures/non-login-user.json` (belum ada).
- Data Dinamis (di-seed hook `before` lewat API, mekanisme disediakan tim FE/BE; dihapus hook `after`): sebelas Non-Login User `Pagination Sebelas {runId}-088 01` sampai `Pagination Sebelas {runId}-088 11` (Active, Division `Operations`) untuk TC-GS-NLU-307, menggantikan `Pagination Sebelas 01-11` Pre-setup agar Pre-setup tidak dihapus (S-06); Search `Pagination Sebelas {runId}-088` menyaring tepat 11 baris dari seeding ini (nama `Impor Satu {runId}-088` tidak memuat `Pagination Sebelas`, sehingga tidak ikut tersaring); Non-Login User `Impor Satu {runId}-088` untuk TC-GS-NLU-483 (Position awal bukan `Driver`, tanpa entri Changelog, disiapkan tim FE/BE lewat jalur seed yang tidak menulis Changelog seperti hasil Import; waktu record dibuat dibaca lewat kemampuan baca data).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pengaturan ukuran halaman (10/25/50/100); input nomor halaman; penghapusan preferensi kolom di browser di hook `after` (disediakan tim FE; spec ini menyimpan konfigurasi kolom untuk TC-GS-NLU-453); pengamatan tooltip hover dan tinggi baris; jam server dan jam browser sinkron untuk perbandingan Last Update (toleransi satu menit, kolom Date berketelitian menit).
- State global: konfigurasi kolom (Temporary User, Temporary Until, Blood Type diaktifkan pada TC-GS-NLU-453), dipulihkan oleh langkah penghubung dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-305: Pagination tabel List: default 10, opsi ukuran halaman, dan navigasi

1. Amati footer pagination
2. Verifikasi default 10 baris per halaman
3. Buka opsi page size
4. Verifikasi opsi page size 10, 25, 50, 100
5. Klik halaman 2
6. Verifikasi halaman 2 menampilkan baris berikutnya (baris halaman 2 berbeda dari baris halaman 1)
7. Ganti page size ke 25
8. Verifikasi tabel kembali ke halaman 1
9. Ganti page size ke 10

### TC-GS-NLU-306: Mengganti sort tidak mengubah nomor halaman dan input nomor halaman tidak valid diabaikan

10. Klik halaman 2
11. Klik header kolom `Division`
12. Verifikasi setelah sort tetap di halaman 2
13. Ketik `0`, lalu `99`, lalu `abc` pada input nomor halaman satu per satu
14. Verifikasi setiap input tidak valid diabaikan dan tabel tetap di halaman 2
15. Klik header kolom `Division` dua kali lagi hingga kembali ke default sort, klik halaman 1

### TC-GS-NLU-308: Nama panjang tampil utuh tanpa dipotong

16. Ketik Search `Fixture.nonLoginUser.namaPanjang.kunciSearch`, tekan Enter
17. Verifikasi nama tampil utuh (wrap natural) tanpa `..`
18. Verifikasi tidak ada tooltip pada sel Name saat kursor diarahkan
19. Verifikasi tinggi baris menyesuaikan
20. Klik `(←)` pada kotak Search

### TC-GS-NLU-453: Isi kolom curated List: Temporary User, Temporary Until, dan Custom Field

21. Klik `⋯` header Actions > `Setup Column...`, centang kolom Temporary User, Temporary Until, dan Blood Type, klik `[Save]`
22. Ketik Search `Rina Marlina`, tekan Enter
23. Verifikasi baris `Rina Marlina`: Temporary User `Yes`
24. Verifikasi baris `Rina Marlina`: Temporary Until tanggal sesuai General Settings
25. Verifikasi baris `Rina Marlina`: Blood Type `O`
26. Ganti isi kotak search dengan `Siti Rahayu`, tekan Enter
27. Verifikasi baris `Siti Rahayu`: Temporary User `No`
28. Verifikasi baris `Siti Rahayu`: Temporary Until `—`
29. Klik `⋯` header Actions > `Setup Column...`, hapus centang kolom Temporary User, Temporary Until, dan Blood Type, klik `[Save]`

### TC-GS-NLU-483: Last Update record hasil Import menampilkan waktu record dibuat

30. Ganti isi kotak search dengan `Impor Satu {runId}-088`, tekan Enter
31. Verifikasi Last Update baris `Impor Satu {runId}-088` terisi (bukan `—`) dengan format General Settings
32. Verifikasi Last Update sama dengan waktu record dibuat (toleransi satu menit)
33. Klik `⋯` > `Edit`, ubah Position menjadi `Driver`, klik `[Save]`
34. Verifikasi toast sukses `Success, non-login user has been updated.`
35. Catat waktu sesudah `[Save]`
36. Verifikasi Last Update baris `Impor Satu {runId}-088` berpindah ke waktu entri Changelog `Edit` yang baru (sama dengan waktu yang dicatat, toleransi satu menit)
37. Klik `(←)` pada kotak Search

### TC-GS-NLU-307: Menghapus baris terakhir di halaman terakhir pindah ke halaman terakhir yang ada

38. Ketik Search `Pagination Sebelas {runId}-088`, tekan Enter
39. Klik halaman 2
40. Hapus satu-satunya baris di halaman 2: klik `⋯` > `Delete`, klik `[Delete]` pada dialog konfirmasi
41. Verifikasi tabel pindah ke halaman 1 (halaman terakhir yang masih ada)

## Notes

- Urutan TC di dalam spec: TC-GS-NLU-307 (menghapus data) berada di akhir spec, dan TC-GS-NLU-308 mendahului TC-GS-NLU-453, mengikuti prinsip aksi menghapus data di akhir (S-10).
- Langkah penghubung (S-03): mengembalikan page size dan halaman, `(←)` yang mengosongkan Search, dan memulihkan kolom Temporary User, Temporary Until, Blood Type pada TC-GS-NLU-453 (S-09). Search untuk menemukan baris target dicatat di sini (R-16). Hook `after` menghapus preferensi kolom sebagai cadangan.
- Asersi tambahan (S-03): TC-GS-NLU-483 menambah langkah "Catat waktu sesudah `[Save]`" untuk perbandingan Last Update dengan toleransi satu menit (S-12). Search `Pagination Sebelas {runId}-088` pada langkah 38 menggantikan Search `Pagination Sebelas` (yang juga menyaring Pre-setup) dan Search `{runId}-088` (yang juga menyaring `Impor Satu {runId}-088`), sehingga hasil tepat 11 baris milik spec (N dari seeding; 8b.10) dan langkah 40 menghapus baris halaman 2 milik rangkaian itu. Nama seed `Pagination Sebelas {runId}-088 NN` dipilih agar `{runId}` berada langsung sesudah `Pagination Sebelas` pada substring Search.
- Di atas 35 langkah, alasan: Spec ini sekitar 41 langkah dan dipertahankan utuh karena seluruh blok satu kelas harness (fungsional, tabel List yang sama) dan berdiri sendiri: kegagalan satu TC tidak membuat TC lain kehilangan makna; TC-GS-NLU-307 memakai data milik spec sehingga kegagalannya tidak memengaruhi blok lain.
- Temuan untuk QA:
  - TC-GS-NLU-308 tidak menyebut nama atau kata kunci record First/Last Name 60 karakter; spec memakai kata kunci fixture baru.
  - TC-GS-NLU-483 tidak menyebut cara menyiapkan record hasil Import tanpa entri Changelog; mekanisme disediakan tim FE/BE. TC-GS-NLU-483 langkah 3 mengubah Position record Pre-setup `Impor Satu`; spec memakai record milik sendiri.
  - TC-GS-NLU-307 langkah 3 ("hapus satu-satunya baris") tidak menyebut langkah Delete; spec memakai row action `⋯` > `Delete` dan dialog konfirmasi `[Delete]` sesuai konvensi dialog konfirmasi.
  - TC-GS-NLU-453 Expected a menyebut Temporary Until "sesuai General Settings" tanpa nilai tanggal; spec mengasersi format tanggal tanpa nilai tetap.
  - TC-GS-NLU-305 Expected a tidak menyebut cara membuka opsi page size selain "Buka opsi page size".
