---
id: TC-AC-ACC-E2E-047-foto-client-create-edit-dan-remove-af
title: "Photo Client: Resize Foto Besar, Ganti, Hapus, dan Remove Staged (Active-Full)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-123
  - TC-AC-ACC-943
  - TC-AC-ACC-966
  - TC-AC-ACC-162
coverage:
  web: automated
---

# Photo Client: Resize Foto Besar, Ganti, Hapus, dan Remove Staged (Active-Full)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-047@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Berkas uji di mesin uji: `foto-uji-besar.jpg` (JPG 3 MB), `foto-uji-a.jpg` (JPG 200 KB), `foto-uji-b.png` (PNG 300 KB). Kemampuan teknis: memilih berkas pada ImagePicker, membaca atribut `src` thumbnail Photo, membuka URL gambar di tab baru, mengamati ukuran berkas gambar, dan mengamati request jaringan.
- Dataset Dinamis: `PT Foto Besar Uji {runId}-047`, `PT Foto Ganti Uji {runId}-047`, `PT Foto Lepas Uji {runId}-047` (dibuat UI); Client `PT Foto Staged {runId}-047` (Active, Default User Activated, atribut Photo tersimpan; setara C-01 pada TC-162). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-123: Foto lebih dari 1 MB di-resize otomatis

1. Klik `[+ New Client]`
2. Pilih foto `foto-uji-besar.jpg` (JPG 3 MB)
3. Verifikasi tidak ada pesan error pada Photo
4. Isi Company Name `PT Foto Besar Uji {runId}-047`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Cabang Menteng"
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, client has been created."
7. Ketik Search `PT Foto Besar Uji {runId}-047`, tekan Enter
8. Klik Company Name `PT Foto Besar Uji {runId}-047` untuk membuka Detail
9. Verifikasi header Detail menampilkan thumbnail Photo (bukan avatar inisial)
10. Buka URL thumbnail Photo di header Detail di tab baru dan catat ukuran berkas
11. Verifikasi gambar tampil dan ukuran berkas maksimal 1 MB

### TC-943: Photo diganti saat Edit, file lama tidak dapat dibuka

12. Klik breadcrumb "Client" untuk kembali ke List
13. Klik `[+ New Client]`
14. Pilih foto `foto-uji-a.jpg` (JPG 200 KB)
15. Isi Company Name `PT Foto Ganti Uji {runId}-047`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Cabang Menteng"
16. Klik `[Submit]`
17. Verifikasi toast sukses "Success, client has been created."
18. Ketik Search `PT Foto Ganti Uji {runId}-047`, tekan Enter
19. Klik Company Name `PT Foto Ganti Uji {runId}-047` untuk membuka Detail
20. Verifikasi header Detail menampilkan thumbnail Photo (bukan avatar inisial)
21. Catat atribut `src` thumbnail Photo header Detail sebagai URL foto A
22. Klik `[Edit]` di header Detail
23. Klik ikon `[✕]` pada thumbnail Photo
24. Pilih foto `foto-uji-b.png` (PNG 300 KB)
25. Klik `[Save]`
26. Verifikasi popup tertutup
27. Verifikasi toast sukses "Success, client has been updated."
28. Verifikasi header Detail menampilkan thumbnail Photo
29. Buka URL foto A di tab baru
30. Verifikasi URL foto A tidak menampilkan gambar (permintaan ke URL itu tidak mengembalikan berkas gambar)

### TC-966: Remove Photo lalu Save, file lama tidak dapat dibuka

31. Klik breadcrumb "Client" untuk kembali ke List
32. Klik `[+ New Client]`
33. Pilih foto `foto-uji-a.jpg` (JPG 200 KB)
34. Isi Company Name `PT Foto Lepas Uji {runId}-047`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Cabang Menteng"
35. Klik `[Submit]`
36. Verifikasi toast sukses "Success, client has been created."
37. Ketik Search `PT Foto Lepas Uji {runId}-047`, tekan Enter
38. Klik Company Name `PT Foto Lepas Uji {runId}-047` untuk membuka Detail
39. Verifikasi header Detail menampilkan thumbnail Photo (bukan avatar inisial)
40. Catat atribut `src` thumbnail Photo header Detail sebagai URL foto A
41. Klik `[Edit]` di header Detail
42. Klik ikon `[✕]` pada thumbnail Photo
43. Verifikasi preview Photo kembali ke upload placeholder
44. Klik `[Save]`
45. Verifikasi popup tertutup
46. Verifikasi toast sukses "Success, client has been updated."
47. Verifikasi header Detail menampilkan avatar inisial (tanpa thumbnail Photo)
48. Buka URL foto A di tab baru
49. Verifikasi URL foto A tidak menampilkan gambar (permintaan ke URL itu tidak mengembalikan berkas gambar)

### TC-162: Remove Photo existing bersifat staged

50. Klik breadcrumb "Client" untuk kembali ke List
51. Ketik Search `PT Foto Staged {runId}-047`, tekan Enter
52. Buka `⋯` baris `PT Foto Staged {runId}-047` lalu klik `Edit`
53. Klik ikon `[✕]` pada thumbnail Photo
54. Verifikasi preview Photo kembali ke upload placeholder
55. Verifikasi tidak ada request hapus foto ke server
56. Klik `[✕]` pada header popup
57. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
58. Klik `[Leave]`
59. Buka `⋯` baris `PT Foto Staged {runId}-047` lalu klik `Edit`
60. Verifikasi thumbnail Photo lama masih tampil (foto tidak berubah)
61. Klik ikon `[✕]` pada thumbnail Photo
62. Klik `[Save]`
63. Verifikasi popup tertutup
64. Verifikasi toast sukses "Success, client has been updated."
65. Verifikasi foto terhapus (avatar inisial) pada baris atau Detail "PT Foto Staged {runId}-047"
66. Klik `[Changelog]` di toolbar List
67. Klik ikon Search di modal Changelog, ketik `PT Foto Staged {runId}-047`, tekan Enter
68. Verifikasi Changelog memuat baris Action `Edit`, Client Name "PT Foto Staged {runId}-047", Field `Photo`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 70 langkah): satu topik (Photo Client), satu role; empat blok membuat dan mengubah datanya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah melebar karena tiap blok memuat Create lalu Edit.
- Langkah penghubung (S-03): Search nama unik, klik Company Name ke Detail, "Klik breadcrumb Client" kembali ke List.
- Temuan untuk QA:
  - TC-162 langkah 10 ("Buka Changelog: Client") tidak menyebut cara menemukan baris; spec memakai Search nama Client unik (baseline nol) di modal Changelog. TC-162 Expected butir d "foto terhapus (avatar inisial)" tidak menyebut layar; spec memeriksa baris atau Detail.
  - TC-123, TC-943, TC-966: Post Condition "dibersihkan oleh reset data uji" tidak punya langkah observasi; cleanup dilakukan hook `after`.
  - Sumber foto B (TC-943) ukuran 300 KB tidak diverifikasi di UI; hanya dipakai sebagai berkas pengganti.
