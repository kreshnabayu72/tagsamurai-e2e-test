---
id: TC-FA-CAT-E2E-053-edit-validasi-code-dan-description
title: "Edit Category: Validasi Code (Helper Text, Batas 15 Karakter, Whitelist, Duplikat, Uppercase) dan Batas Description 360 Karakter"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-536
  - TC-FA-CAT-186
  - TC-FA-CAT-187
  - TC-FA-CAT-188
  - TC-FA-CAT-189
  - TC-FA-CAT-190
coverage:
  web: automated
---

# Edit Category: Validasi Code (Helper Text, Batas 15 Karakter, Whitelist, Duplikat, Uppercase) dan Batas Description 360 Karakter

## Prerequisites

- Mode: FE+BE (backend nyata; nilai tersimpan diasersi lewat UI dan pembacaan state BE).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data milik spec (seed lewat API di hook `before`, disediakan tim FE/BE): kategori L1 leaf `Furniture {runId}-053` (Code `FURN053`, Total Asset 0) menjadi target Edit (S-06). Blok TC-FA-CAT-186 (Code 15 karakter `C`) dan TC-FA-CAT-189 (Description 360 karakter `D`) menyimpan perubahan. Pemulihan `Furniture {runId}-053` (Name, Code, Description) ke nilai seed lewat API dijalankan sebagai langkah penghubung sesudah tiap blok yang menyimpan; hook `after` menghapus kategori itu. Data Pre-setup #20 (CatMain) hanya dibaca: Code `TOOL` milik `Tools` dipakai sebagai nilai duplikat yang diketik pada TC-FA-CAT-188 dan Save diblok sehingga `Tools` tidak diubah. Efek: entri Changelog CatMain bertambah (audit trail permanen; tidak ada asersi jumlah); suite berjalan serial. Nilai "15 karakter `C`", "16 karakter `C`", "360 karakter `D`", dan "361 karakter `D`" tepat sejumlah itu tanpa suffix run (nilai uji batas, bukan nama entitas).
- Kemampuan teknis: membaca state BE kategori `Furniture {runId}-053` (disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-536: Helper text Code tampil sejak awal dan dipulihkan

1. Klik elipsis (⋯) pada baris `Furniture {runId}-053` > `Edit`
2. Verifikasi helper text `Letters, numbers, hyphens, underscores, and dots only` tampil sejak popup Edit dibuka
3. Ketik Code `FU!`
4. Verifikasi helper text digantikan `Code contains invalid characters` saat error aktif
5. Hapus karakter `!` pada Code
6. Verifikasi helper text `Letters, numbers, hyphens, underscores, and dots only` tampil kembali

### TC-FA-CAT-186: Code 15 karakter diterima dan 16 karakter menampilkan error

7. Isi Code dengan 15 karakter `C`
8. Klik `[Save]`
9. Verifikasi 15 karakter diterima: popup Edit tertutup tanpa error
10. Pulihkan `Furniture {runId}-053` ke nilai seed lewat API
11. Klik elipsis (⋯) pada baris `Furniture {runId}-053` > `Edit`
12. Isi Code dengan 16 karakter `C`
13. Verifikasi pesan `Max. 15 characters` tampil langsung
14. Klik `[Save]`
15. Verifikasi Save diblok: popup tetap terbuka dan Code tersimpan tidak berubah (dibaca dari state BE)

### TC-FA-CAT-187: Karakter di luar whitelist pada Code

16. Ketik Code `FU RN!`
17. Verifikasi pesan `Code contains invalid characters` tampil langsung saat mengetik

### TC-FA-CAT-188: Code milik kategori lain ditolak, Code milik sendiri diterima

18. Ubah Code menjadi `TOOL`
19. Tunggu 500ms
20. Verifikasi pesan `Code already exists` tampil
21. Klik `[Save]`
22. Verifikasi Save diblok: popup tetap terbuka dan Code tersimpan tidak berubah (dibaca dari state BE)
23. Ubah Code kembali menjadi `FURN053`
24. Tunggu 500ms
25. Verifikasi tidak ada error pada Code karena record sendiri dikecualikan

### TC-FA-CAT-189: Description 360 karakter diterima dan 361 karakter menampilkan error

26. Isi Description dengan 360 karakter `D`
27. Klik `[Save]`
28. Verifikasi 360 karakter diterima: popup Edit tertutup tanpa error
29. Pulihkan `Furniture {runId}-053` ke nilai seed lewat API
30. Klik elipsis (⋯) pada baris `Furniture {runId}-053` > `Edit`
31. Isi Description dengan 361 karakter `D`
32. Verifikasi pesan `Max. 360 characters` tampil langsung
33. Klik `[Save]`
34. Verifikasi Save diblok: popup tetap terbuka dan Description tersimpan tidak berubah (dibaca dari state BE)

### TC-FA-CAT-190: Code di-uppercase otomatis

35. Ketik Code `fu-rn`
36. Verifikasi field Code menampilkan `FU-RN`
37. Klik icon close (✕)
38. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
39. Klik `[Leave]`

## Notes

- Mode: FE+BE. Enam blok berdiri sendiri (validasi Code dan Description pada satu popup Edit) sehingga jumlah langkah (39) sedikit melewati sekitar 35; kegagalan satu blok tidak menghilangkan makna blok lain.
- Urutan: TC-FA-CAT-536 ditempatkan pertama karena Expected a mensyaratkan popup yang baru dibuka; blok sesudahnya memakai popup yang sama tanpa dibuka ulang selama tidak ada Save sukses (S-10). Popup dibuka ulang (langkah 11, 30) sesudah Save sukses.
- Langkah penghubung (S-03, S-08, S-09): langkah 10 dan 29 (memulihkan `Furniture {runId}-053`), langkah 14, 21, dan 33 (klik `[Save]` untuk Expected "Save diblok" pada TC yang tidak menuliskan klik Save, dicatat di Temuan untuk QA), langkah 37 sampai 39 (menutup form dirty secara deterministik).
- Temuan untuk QA:
  - TC-FA-CAT-536 dan 186 sampai 190 menyebut baris `Furniture` Pre-setup sebagai target Edit; spec memakai kategori milik spec `Furniture {runId}-053` dengan Code `FURN053` (S-06) agar data Pre-setup tidak berubah.
  - TC-FA-CAT-186, 188, dan 189 tidak menyebut klik `[Save]` pada langkah yang memunculkan error (16 karakter, `TOOL`, 361 karakter), padahal Expected "Save diblok"; spec menambah klik Save (langkah 14, 21, 33).
  - TC-FA-CAT-186 dan 189 menyebut "diterima" tanpa teks toast; spec mengasersi popup tertutup tanpa error.
  - TC-FA-CAT-190 tidak punya Expected persistensi; spec hanya mengasersi tampilan field.
- Spec melewati 35 langkah (39 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri.
