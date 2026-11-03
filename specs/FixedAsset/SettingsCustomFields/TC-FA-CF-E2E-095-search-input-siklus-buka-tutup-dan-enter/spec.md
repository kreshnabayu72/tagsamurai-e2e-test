---
id: TC-FA-CF-E2E-095-search-input-siklus-buka-tutup-dan-enter
title: "Search: Siklus Input, Enter, Icon Silang, dan Panah Kembali"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-357
  - TC-FA-CF-358
  - TC-FA-CF-359
  - TC-FA-CF-360
coverage:
  web: automated
---

# Search: Siklus Input, Enter, Icon Silang, dan Panah Kembali

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena asersi bergantung pada nama baris; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12) berisi delapan field: `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`. Jumlah delapan baris diturunkan dari seeding baseline dan tampil seluruhnya pada satu halaman (ukuran halaman bawaan 10).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan fokus input, isi kotak Search, dan tooltip pada Page Object.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-CF-357: Klik ikon Search membuka input

1. Arahkan kursor ke ikon Search (belum diklik)
2. Verifikasi tooltip `Search` tampil
3. Klik ikon Search
4. Verifikasi input pencarian melebar
5. Verifikasi kursor otomatis fokus di dalam input
6. Verifikasi placeholder `Search custom field...` tampil
7. Klik `(←)`

### TC-FA-CF-358: Search tidak real-time dan baru menyaring setelah Enter

8. Klik ikon Search
9. Ketik `serial` tanpa menekan Enter
10. Verifikasi icon `(✕)` muncul di dalam input
11. Verifikasi tabel belum tersaring (seluruh delapan baris tab General masih tampil)
12. Tekan Enter
13. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag`

### TC-FA-CF-359: Icon silang mengosongkan input tanpa mereset tabel hingga Enter pada input kosong

14. Klik `(←)`
15. Klik ikon Search
16. Ketik `serial`, tekan Enter
17. Klik icon `(✕)`
18. Verifikasi isi input kosong
19. Verifikasi search bar tetap terbuka
20. Verifikasi input tetap fokus
21. Verifikasi tabel masih menampilkan hasil `serial` (hanya baris `Asset Serial Tag`)
22. Tekan Enter pada input kosong
23. Verifikasi tabel kembali menampilkan seluruh delapan baris

### TC-FA-CF-360: Icon panah kembali menutup search bar dan langsung mereset tabel

24. Klik `(←)`
25. Klik ikon Search
26. Ketik `serial`, tekan Enter
27. Klik icon panah `(←)` di kiri toolbar
28. Verifikasi kotak pencarian menutup menjadi ikon Search
29. Verifikasi keyword Search dikosongkan
30. Verifikasi tabel langsung menampilkan seluruh delapan baris

## Notes

- Spec memuat 30 langkah, di bawah ambang sekitar 35 langkah. Dataset dan akun tunggal (Total Control Company Alpha, tab General).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 14, dan 24 (`(←)` menutup input dan mengosongkan keyword sebelum TC berikutnya). Klik ikon Search ditulis eksplisit di langkah 3, 8, 15, dan 25 karena spec ini menguji siklus input (bagian 8b butir 9).
- Urutan langkah TC-FA-CF-357 mengikuti urutan state (bagian 8b butir 5): kursor diarahkan ke ikon Search dan tooltip diasersi sebelum ikon diklik, walau TC menulis langkah klik lebih dulu.
- Langkah 17 sampai 21 mengasersi Expected a TC-FA-CF-359 yang bermajemuk (input kosong, search bar tetap terbuka, fokus, tabel masih menampilkan hasil `serial`) dan dipecah satu `Verifikasi` per klausa (S-01).
- Temuan untuk QA:
  - TC-FA-CF-358 Expected a menyebut "tabel belum tersaring" tanpa menyebut jumlah baris; spec memakai seluruh delapan baris baseline (jumlah itu disebut TC-FA-CF-359 Expected b dan TC-FA-CF-360).
  - TC-FA-CF-360 Expected menyebut "keyword dikosongkan" tanpa menyebut cara memeriksanya setelah kotak menutup; langkah 29 membaca nilai keyword Search lewat Page Object (kemampuan teknis disediakan tim FE).
  - Tooltip pada TC-FA-CF-357 Expected c disebut "tooltip `Search`" tanpa menyebut jeda hover; spec mengasersi segera setelah kursor diarahkan.
  - TC-FA-CF-357 sampai TC-FA-CF-360 tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
