---
id: TC-FA-LBL-E2E-038-modal-create-edit-label-interaksi-live-preview-escape-dan-debounce-keunikan
title: "Modal Create/Edit Label: Live Preview per karakter, Escape pada Color Picker, dan debounce cek keunikan"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:interaction-patterns/real-time-live-preview
  - FALB:interaction-patterns/escape-key
  - FALB:interaction-patterns/debounced-uniqueness-check
coverage:
  web: automated
---

# Modal Create/Edit Label: Live Preview per karakter, Escape pada Color Picker, dan debounce cek keunikan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-67` (label seed `Mdl-{runId}-038` berwarna `#3B82F6`, dibuat lewat sesi API di hook `before`; dipakai sebagai nama duplikat pada langkah 17). `DU-69` (nama uji Live Preview `Preview-{runId}-038`, diketik karakter demi karakter).
- Tabel "Karakter yang diketik satu per satu" (dipakai langkah 2 dan 3): `P`, `r`, `e` (tiga karakter pertama nama `DU-69`).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding dan penghapusan label. `Spectra.intercept()` untuk mencatat permintaan cek keunikan nama label dan untuk menggagalkannya (endpoint dari openapi dan LLD modul, ditentukan di tahap script).
- Jeda nyata: dua langkah menunggu 1 detik (langkah 18 dan 24), pilihan spec ini untuk memberi kesempatan debounce 500 ms selesai.
- State global: tidak ada yang diubah. Hook `after` melepas intercept bila masih terpasang dan menghapus label `DU-67` lewat sesi API walau spec gagal di tengah.

## Test Steps

### FALB:interaction-patterns/real-time-live-preview: Live Preview per karakter dan per titik warna

1. Klik `[+ Label]`
2. Untuk setiap karakter pada tabel "Karakter yang diketik satu per satu" (langkah 2 sampai 3): ketik karakter itu pada field Label Name
3. Verifikasi Live Preview menampilkan seluruh teks yang sudah diketik sampai karakter itu
4. Ketik sisa nama `DU-69` setelah tiga karakter pertama pada field Label Name
5. Verifikasi Live Preview menampilkan nama `DU-69` utuh
6. Klik Swatch Trigger
7. Klik swatch preset baris 1 kolom 1 (`#EF4444`)
8. Verifikasi chip Live Preview berlatar warna `#EF4444` seketika
9. Klik satu titik pada Kanvas Warna Kustom
10. Verifikasi chip Live Preview berlatar warna yang sama dengan nilai kolom Hex setelah titik kanvas diklik

### FALB:interaction-patterns/escape-key: Escape menutup Color Picker Overlay tanpa menutup Modal

11. Verifikasi Color Picker Overlay masih terbuka
12. Tekan Escape
13. Verifikasi Color Picker Overlay tertutup
14. Verifikasi Modal `Create Label` tetap terbuka dengan field Label Name berisi `DU-69`

### FALB:interaction-patterns/debounced-uniqueness-check: Debounce cek keunikan nama

15. Klik `[Clear Field]`
16. Pasang intercept pencatat permintaan cek keunikan nama label tanpa mengubah respons
17. Ketik Label Name `DU-67` berturut-turut tanpa jeda
18. Tunggu 1 detik tanpa berpindah field
19. Verifikasi inline error `Label name already exists` tampil di bawah field Label Name tanpa field kehilangan fokus
20. Verifikasi tepat satu permintaan cek keunikan tercatat sesudah ketikan terakhir
21. Lepas intercept pencatat
22. Pasang intercept yang menggagalkan permintaan cek keunikan nama label
23. Ganti isi field Label Name dengan `DU-69`
24. Tunggu 1 detik tanpa berpindah field
25. Verifikasi tidak ada pesan error inline di bawah field Label Name
26. Verifikasi tombol `[Submit]` Enabled
27. Lepas intercept yang menggagalkan permintaan
28. Klik `[Clear Field]`
29. Klik `[✕]` pada header Modal Create Label

## Notes

- Langkah penghubung (S-03): langkah 1 (membuka modal), langkah 6 (membuka Color Picker Overlay), langkah 15 dan 28 (mengosongkan form), langkah 16, 21, 22, dan 27 (memasang dan melepas intercept), langkah 18 dan 24 (jeda 1 detik), langkah 29 (menutup modal yang sudah bersih; form kembali ke keadaan awal Create sehingga dialog `Unsaved Changes` tidak muncul).
- Langkah 2 dan 3 diulang tiga kali (satu per karakter pada tabel Prerequisites); `Verifikasi` tetap satu per karakter.
- Anchor positif (bagian 8b butir 2): langkah 19 membuktikan pengecekan keunikan berjalan sebelum langkah 25 mengasersi ketiadaan pesan error saat permintaan digagalkan; langkah 11 menjadi anchor langkah 13.
- Pengecualian P-5 butir (b): langkah 22 sampai 27 adalah satu blok kegagalan request cek keunikan (kelas b ringan) pada spec fungsional yang permukaannya sama (field Label Name); blok tanpa harness eksternal dan tanpa state berat. Intercept dilepas segera pada langkah 27 (S-09).
- Interval debounce 500 ms diasersi lewat satu permintaan cek keunikan sesudah ketikan terakhir (langkah 20), bukan lewat pengukuran waktu tepat.
