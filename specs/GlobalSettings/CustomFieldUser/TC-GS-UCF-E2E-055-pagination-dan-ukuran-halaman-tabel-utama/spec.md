---
id: TC-GS-UCF-E2E-055-pagination-dan-ukuran-halaman-tabel-utama
title: "Pagination dan Ukuran Halaman Tabel Custom Field: Next/Prev, Opsi Page Size, Nomor Halaman Tidak Valid, Retensi F5, dan Hapus Baris Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-230
  - TC-GS-UCF-232
  - TC-GS-UCF-234
  - TC-GS-UCF-233
coverage:
  web: automated
---

# Pagination dan Ukuran Halaman Tabel Custom Field: Next/Prev, Opsi Page Size, Nomor Halaman Tidak Valid, Retensi F5, dan Hapus Baris Terakhir

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Untuk TC-GS-UCF-233 spec berganti ke Total Control Client B (Lina Kusuma, Modified By `Lina K`) `totalControl_automated_qaTeam2@qwertysystem.net` dengan `Spectra.env.GS_CLIENTB_TC_PASSWORD` lewat langkah ganti akun eksplisit (langkah 43); hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini, tanpa suffix; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.preset14`): 6 Custom Field `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, dan `Joining Date`; dipakai sebagai precondition TC (total 14 baris), tidak diasersi satu per satu.
- Data Dinamis Population D-01 (8 field; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.population`): `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`; Active; Modified By `Sari D`. Di-seed lewat API oleh akun Total Control Client A di hook `before` (mekanisme disediakan tim FE/BE, endpoint tidak ditulis di spec). Nama literal tanpa suffix karena kata kunci Search `o` dan jumlah 14 baris (halaman 1 berisi 10 baris, halaman 2 berisi 4 baris) bergantung pada data (pengecualian Population, S-12); seeding idempotent (dilewati bila sudah ada); cleanup hanya menghapus yang dibuat hook spec ini. Total Custom Field Client A tepat 14 saat spec berjalan.
- Data Pre-setup Client B (tetap di environment, tidak diubah spec ini): 10 Custom Field bertipe Text, Active, Required `No`, Modified By `Lina K` (fixture backend; disediakan tim FE/BE). Data Dinamis milik spec: `Client B Eleven {runId}-055` (D-87: Text; field ke-11 Client B) di-seed lewat API oleh akun Total Control Client B di hook `before` secara idempotent (dilewati bila sudah ada; mekanisme disediakan tim FE/BE) dan dihapus sendiri oleh spec ini (TC-GS-UCF-233 dan hook `after`), sehingga Client B memiliki tepat 11 field dan halaman 2 pada ukuran halaman 10 berisi 1 baris; fixture baru `Fixture.customFieldUser.paginationSeed055`.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field (Client A); spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`. Setelah ganti akun ke Client B (langkah 43), halaman dibuka lewat langkah eksplisit (langkah 44).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Client B Eleven {runId}-055` bila masih ada dan field Population yang dibuat hook `before`; kembalikan sesi ke Total Control Client A; pulihkan ukuran halaman ke 10 dan sort ke netral.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor Client A dan Client B dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pembacaan halaman aktif, jumlah baris, opsi page size, dan input nomor halaman; muat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form terbuka).
- State global: ukuran halaman diubah ke 25 dan dikembalikan ke 10 oleh TC-GS-UCF-230 (langkah 9 dan 11) dan oleh TC-GS-UCF-234 (langkah 27 dan 33). Aksi Delete TC-GS-UCF-233 menghapus `Client B Eleven {runId}-055` milik spec dan ditaruh paling akhir.

## Test Steps

### TC-GS-UCF-230: Pagination, opsi page size, Next/Prev, dan input nomor halaman

1. Klik Next
2. Verifikasi halaman 2 aktif
3. Verifikasi halaman 2 menampilkan 4 baris
4. Klik Prev
5. Verifikasi halaman 1 aktif
6. Buka page size
7. Verifikasi opsi page size tepat `10`, `25`, `50`, dan `100`
8. Verifikasi opsi `All` tidak ada
9. Pilih 25
10. Verifikasi ukuran 25 menampilkan 14 baris dalam 1 halaman
11. Ubah ukuran halaman kembali ke 10
12. Ketik `2` di input halaman, tekan Enter
13. Verifikasi tabel langsung berada di halaman 2

### TC-GS-UCF-232: Nomor halaman tidak valid diabaikan

14. Klik Prev
15. Verifikasi halaman 1 aktif
16. Ketik `0` di input halaman, tekan Enter
17. Verifikasi tabel tetap di halaman 1
18. Verifikasi tidak ada error
19. Ketik `99` di input halaman, tekan Enter
20. Verifikasi tabel tetap di halaman 1
21. Verifikasi tidak ada error
22. Ketik `abc` di input halaman, tekan Enter
23. Verifikasi tabel tetap di halaman 1
24. Verifikasi tidak ada error

### TC-GS-UCF-234: Refresh F5 mempertahankan Search, Sort, page size non-default, dan halaman

25. Ketik Search `o`, tekan Enter
26. Klik header Field Name dua kali (descending)
27. Ubah ukuran halaman tabel ke 25
28. Tekan F5
29. Verifikasi tombol Download tampil pada Table Tools (halaman termuat ulang)
30. Verifikasi keyword `o` tetap terisi
31. Verifikasi sort Field Name descending tetap aktif
32. Verifikasi ukuran halaman 25 tetap
33. Ubah ukuran halaman tabel ke 10
34. Klik Next (pindah ke halaman 2)
35. Tekan F5
36. Verifikasi tombol Download tampil pada Table Tools (halaman termuat ulang)
37. Verifikasi keyword `o` tetap terisi
38. Verifikasi sort Field Name descending tetap aktif
39. Verifikasi ukuran halaman 10 tetap
40. Verifikasi halaman 2 tetap aktif
41. Klik header Field Name sekali lagi (sort kembali netral)
42. Klik `(←)`

### Ganti akun ke Total Control Client B

43. Ganti akun: Logout, lalu login sebagai Total Control Client B (Lina Kusuma) `totalControl_automated_qaTeam2@qwertysystem.net`
44. Buka Global Settings > User > Custom Field

### TC-GS-UCF-233: Menghapus baris terakhir di halaman terakhir memindahkan tabel ke halaman terakhir yang masih ada

45. Pindah ke halaman 2
46. Klik `⋯` pada baris `Client B Eleven {runId}-055`, klik Delete
47. Klik [Delete] pada dialog konfirmasi
48. Verifikasi toast sukses "Success, custom field has been deleted."
49. Verifikasi tabel berpindah ke halaman 1
50. Verifikasi halaman 1 menampilkan 10 baris

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 50 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu topik dan satu dataset (Pagination tabel utama), tanpa mengubah data Pre-setup atau Population; bagian Client B (langkah 43 sampai 50) memakai Step ganti akun eksplisit dan tetap bermakna walau bagian Client A gagal keras (bagian 3 konvensi, pengecualian beda akun), dan TC-GS-UCF-233 menghapus data sehingga berada paling akhir.
- Urutan TC tidak mengikuti urutan nomor TC sumber: TC-GS-UCF-233 (Client B, menghapus data) ditaruh paling akhir (prinsip 3 butir 5 konvensi) dan memakai Step ganti akun eksplisit (langkah 43 dan 44); bagian itu tetap bermakna walau bagian Client A gagal keras. Dependensi data TC-GS-UCF-233 (Client B memiliki 11 field) dipenuhi oleh seeding `Client B Eleven {runId}-055` di hook `before`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 (ukuran halaman kembali ke 10 sesuai langkah 4 TC-GS-UCF-230 "Kembali ke size 10"); langkah 14 (kembali ke halaman 1 agar "halaman sekarang" pada TC-GS-UCF-232 terdefinisi); langkah 41 dan 42 (sort kembali netral dan `(←)` menutup Search); langkah 43 dan 44 (ganti akun dan buka halaman Client B); langkah 45 (pindah ke halaman 2 sesuai langkah 1 TC-GS-UCF-233).
- Verifikasi tambahan di luar Expected TC (S-03): langkah 15 (halaman 1 aktif sebagai baseline sebelum input tidak valid), langkah 29 dan 36 (halaman termuat ulang sesudah F5 sebagai anchor sebelum asersi keadaan Search, Sort, dan ukuran halaman; aturan absence sesudah F5).
- Pembagian TC lintas spec: Search tabel utama ada di spec 051; Filter Panel di spec 052; kombinasi Search, Filter, Sort, dan reset halaman (TC-GS-UCF-231) di spec 053; Sort di spec 054; Setup Column di spec 056.
- Temuan untuk QA:
  - TC-GS-UCF-230 langkah 4 menulis "Kembali ke size 10, ketik `2`" tanpa menyebut apakah halaman aktif sebelumnya 1; spec kembali ke ukuran 10 lalu mengetik `2` (langkah 11 dan 12).
  - TC-GS-UCF-232 tidak menyebut halaman awal ("halaman sekarang"); spec memulai dari halaman 1.
  - TC-GS-UCF-234 tidak menyebut urutan antara F5 pertama dan pindah halaman; hasil Search `o` harus lebih dari 10 baris agar halaman 2 ada (kolom Required memuat `No` sehingga 11 field Required No selalu cocok).
  - Data Client B (keputusan K-9 B, 2026-10-29; TC-GS-UCF-206 dan 233 serta tabel Data Uji telah disesuaikan): Pre-setup Client B adalah 10 field; `Client B Eleven` (D-87) adalah data Dinamis milik spec ini yang di-seed idempotent di hook `before` dan dihapus sendiri (TC-GS-UCF-233), sehingga total 11 saat langkah 45 dan Eleven tidak tertinggal di Pre-setup. Spec 052 hanya membaca 10 field Pre-setup dan tidak bergantung pada Eleven.
  - TC-GS-UCF-233 mengasumsikan `Client B Eleven` berada di halaman 2 (baris ke-11) pada urutan default; urutan default Field Name A-Z menaruh `Client B Eleven` sebelum `Client B Field` (D-85), sehingga kondisi ini bergantung pada nama 9 field Pre-setup lain yang tidak tercantum di TC. Nama field Client B disediakan tim FE/BE.
  - TC-GS-UCF-233 Post Condition tidak ada; data dihapus oleh aksi dan hook `after` sebagai cadangan.
  - Email akun Total Control Client B dari Tabel Data Uji Pre-setup TC; nama env `GS_CLIENTB_TC_PASSWORD` sudah terdaftar di `.env.example`.
