---
id: TC-GS-BRAND-E2E-062-log-absence-no-op-skip-cancel-dan-import
title: "Tidak Ada Pencatatan Log untuk Edit No-Op, Delete Dibatalkan atau Ditolak, Import Brand, dan Brand yang Dilewati"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-210
  - TC-GS-BRAND-211
  - TC-GS-BRAND-212
  - TC-GS-BRAND-292
  - TC-GS-BRAND-78
  - TC-GS-BRAND-79
coverage:
  web: automated
---

# Tidak Ada Pencatatan Log untuk Edit No-Op, Delete Dibatalkan atau Ditolak, Import Brand, dan Brand yang Dilewati

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini karena aksinya No-Op, dibatalkan, atau ditolak; tanpa suffix `{runId}`): `Orion Tech` (bebas relasi), `Acme Corp` (in-use: FAMS Asset Name Forklift), `Zenith Corp` (in-use: FAMS Drill).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before` oleh akun Total Control:
  - `Harbor Tech {runId}-062` dan `Linear Dynamics {runId}-062`: dua brand bebas relasi (milik spec sendiri, bukan Population D-01, karena dihapus di TC-GS-BRAND-210; setara dependensi TC-GS-BRAND-118).
  - `Imported Co {runId}-062` (D-29): dibuat lewat job Import Type Brand yang dijalankan API di hook `before` (sesi uji ini), sehingga tercatat satu entri Changelog: Import. Hook `before` mencatat waktu job selesai sebagai `importJobTime` (presisi sama dengan kolom `Date` Changelog: Import). Changelog: Import hanya memuat kolom `Date | Action | Data | Modified By` tanpa nama file (`global-settings/import/PRD/import.md` §8.1), sehingga entri job ini dikenali lewat `Date` = `importJobTime`.
- Kemampuan teknis: menjalankan job Import Type Brand lewat API dan mencatat waktu selesainya (`importJobTime`); job ini dijalankan dengan selisih waktu dari job Import Brand milik spec `TC-GS-BRAND-E2E-067-brand-hasil-import-edit-dan-hapus` yang terbaca pada presisi kolom `Date`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Harbor Tech`, `Linear Dynamics`, dan `Imported Co` bersuffix `{runId}-062` bila masih ada, dan pulihkan page size tabel Brand ke 10 serta seleksi dan Search tabel ke default.
- Tabel Brand berurut A-Z dengan page size 10 dan Client A punya lebih dari satu halaman brand: `Orion Tech` berada setelah brand Population (A-L) dan `Zenith Corp` paling akhir, sehingga keduanya tidak dijamin tampil di halaman 1. Baris `Orion Tech` dicari lewat Search; pencentangan `Harbor Tech`, `Linear Dynamics`, dan `Zenith Corp` sekaligus memakai page size 50 (opsi tersedia pada paginasi tabel).
- Tidak ada state global yang diubah.
- TC-GS-BRAND-210, 211, 212, 292, 78, 79: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-211: Edit No-Op tidak menghasilkan log (varian TC-GS-BRAND-78 dan TC-GS-BRAND-79)

1. Buka Changelog Brand, Search `Orion Tech`, catat jumlah entri Orion Tech di Changelog
2. Buka Tab System Log Sari Dewi (Global Settings > User > Detail Sari Dewi), Search `Orion Tech`, catat jumlah entri Orion Tech di System Log
3. Buka Global Settings > Activity Log, Search `Orion Tech`, catat jumlah entri Orion Tech di Activity Log
4. Buka Global Settings > Master Reference > Brand, Search `Orion Tech` pada tabel Brand, catat Last Updated baris Orion Tech

### TC-GS-BRAND-78: Save Edit tanpa perubahan nilai adalah No-Op

5. Klik `⋯` pada baris Orion Tech > Edit
6. Klik [Save] tanpa mengubah Brand Name
7. Verifikasi toast netral: "No changes to save."
8. Verifikasi modal tertutup
9. Verifikasi Last Updated Orion Tech tidak berubah

### TC-GS-BRAND-79: Edit yang hanya mengubah huruf besar kecil atau spasi tepi adalah No-Op

10. Search `Orion Tech` pada tabel Brand, klik `⋯` pada baris Orion Tech > Edit
11. Ubah Brand Name menjadi ` ORION TECH ` (diapit spasi)
12. Klik [Save]
13. Verifikasi toast netral: "No changes to save."
14. Verifikasi tabel tetap menampilkan `Orion Tech`
15. Verifikasi Last Updated Orion Tech tidak berubah

### Pemeriksaan ulang tiga surface (lanjutan TC-GS-BRAND-211)

16. Buka Changelog Brand, Search `Orion Tech`
17. Verifikasi Changelog: jumlah entri Orion Tech tidak bertambah dari langkah 1
18. Buka Tab System Log Sari Dewi, Search `Orion Tech`
19. Verifikasi System Log Sari Dewi: jumlah entri Orion Tech tidak bertambah dari langkah 2
20. Buka Global Settings > Activity Log, Search `Orion Tech`
21. Verifikasi Activity Log: jumlah entri Orion Tech tidak bertambah dari langkah 3

### TC-GS-BRAND-212: Delete in-use dan Cancel tidak menghasilkan log

22. Buka Global Settings > Master Reference > Brand, Search `Acme Corp`, klik `⋯` pada baris Acme Corp > Delete → dialog `Cannot Delete Brand` tampil, klik [OK]
23. Search `Orion Tech` pada tabel Brand, klik `⋯` pada baris Orion Tech > Delete → dialog `Delete Brand` tampil, klik [Cancel]
24. Buka Changelog, filter Action `Delete`, Search `Acme Corp`
25. Verifikasi tidak ada entri Delete Acme Corp
26. Verifikasi tidak ada entri Delete Orion Tech setelah Search Changelog diganti menjadi `Orion Tech`

### TC-GS-BRAND-292: Brand hasil Import tidak membuat entri Changelog Brand

27. Kosongkan filter Action pada Changelog Brand
28. Search `Imported Co {runId}-062` di Changelog: Brand
29. Verifikasi Changelog: Brand tidak memuat entri untuk `Imported Co {runId}-062` (`No results found`)
30. Tutup Changelog: Brand, buka Global Settings > Import
31. Klik [Changelog] di header halaman Import → modal `Changelog: Import` tampil
32. Verifikasi Changelog: Import memuat satu entri Action `Import Brand` dengan `Date` = `importJobTime` (job yang dijalankan hook `before` spec ini)

### TC-GS-BRAND-210: Bulk Delete campuran tidak mencatat brand yang dilewati

33. Tutup Changelog: Import, buka Global Settings > Master Reference > Brand, ubah page size tabel menjadi 50, kosongkan Search, lalu centang baris `Harbor Tech {runId}-062`, `Linear Dynamics {runId}-062`, dan Zenith Corp (in-use)
34. Klik `Bulk Action` > `Delete`
35. Klik [Continue] pada dialog Bulk Delete campuran
36. Verifikasi toast sukses: "Success, brand has been deleted. Some items were skipped."
37. Buka Changelog, filter Action `Delete`
38. Verifikasi entri Delete `Harbor Tech {runId}-062` ada di Changelog
39. Verifikasi entri Delete `Linear Dynamics {runId}-062` ada di Changelog
40. Search `zenith` di Changelog
41. Verifikasi tidak ada entri Delete Zenith Corp di Changelog
42. Buka Tab System Log Sari Dewi, Search `Zenith`
43. Verifikasi tidak ada entri Delete Zenith Corp di System Log
44. Buka Global Settings > Activity Log, Search `Zenith`
45. Verifikasi tidak ada entri Delete Zenith Corp di Activity Log

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Spec ini kelas g (asersi absence) untuk aksi UI tunggal; asersi absence dua sesi dan request langsung ke server (TC-GS-BRAND-213 dan TC-GS-BRAND-227 Expected Result b) ada di spec `TC-GS-BRAND-E2E-075-log-absence-dua-sesi-dan-request-langsung`. TC-GS-BRAND-123 dan TC-GS-BRAND-291 berupa asersi jumlah entri dan ada di spec `TC-GS-BRAND-E2E-026-konflik-delete-dua-admin`.
- Urutan TC di spec berbeda dari urutan sumber: 211 (varian 78 dan 79), 212, 292 (tanpa menghapus data) dahulu, lalu 210 yang menghapus data paling akhir (prinsip 5).
- TC-GS-BRAND-78 dan TC-GS-BRAND-79 dijalankan sebagai dua varian dari Langkah Uji TC-GS-BRAND-211 (langkah 5 sampai 15); Post Condition keduanya ("Tidak ada entri log baru") diverifikasi pada langkah 17, 19, dan 21 setelah kedua varian, dengan jumlah entri sebelum (langkah 1 sampai 3) sebagai pembanding.
- Langkah penghubung: langkah 4 (mencatat Last Updated Orion Tech sebagai pembanding TC-GS-BRAND-78 Expected Result c dan TC-GS-BRAND-79 Expected Result c), langkah 22 dan 33 (kembali ke tabel Brand), Search `Orion Tech` pada langkah 4, 10, dan 23 (baris target dicari dulu; Search pada langkah 4 juga menjadi dasar langkah 5), ubah page size menjadi 50 pada langkah 33 (agar ketiga brand tampil sekaligus untuk dicentang; dipulihkan ke 10 di hook `after`), langkah 27 (mengosongkan filter Action `Delete` dari langkah 24 agar asersi absence langkah 29 tidak tersaring), langkah 30 dan 31 (pindah dari Changelog: Brand ke modal Changelog: Import pada header halaman Global Settings > Import).
- Brand `Harbor Tech` dan `Linear Dynamics` pada TC sumber (Population D-01) diganti brand milik spec bersuffix agar tidak menghapus Population yang dipakai spec lain. `Zenith Corp` tidak terhapus karena dilewati (in-use).
- Kebutuhan pencocokan entri Changelog: Import lewat `Date` dan kemampuan mencatat `importJobTime` sudah dicatat sebagai kebutuhan di Prerequisites.
- Temuan untuk QA: TC-GS-BRAND-292 Langkah 2 ("Tutup, buka Changelog: Import") tidak menyebut lokasi Changelog: Import. Modal itu dibuka lewat tombol [Changelog] di header halaman Global Settings > Import (`global-settings/import/PRD/import.md` §8.1), bukan di halaman Brand; spec menambahkan navigasi pada langkah 30 dan 31 sebagai penghubung.
- Alasan spec tidak dipecah (45 langkah): seluruhnya satu kelas harness (asersi absence log, kelas g) dengan satu set data dan satu hook seeding; tiap blok TC tetap bermakna bila dipotong, tetapi urutan non-destruktif lalu destruktif (prinsip 5) dan jejak jumlah entri sebelum/sesudah (langkah 1 sampai 3 dan 16 sampai 21) mengikat blok-blok itu dalam satu eksekusi.
