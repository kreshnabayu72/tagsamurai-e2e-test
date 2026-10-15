---
id: TC-AC-PP-E2E-018-edit-active-berubah-oleh-admin-lain
title: "Versi Active Berubah oleh Admin Lain Saat Modal Edit Dibuka atau Sedang Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-47
  - TC-AC-PP-48
  - TC-AC-PP-95
coverage:
  web: automated
---

# Versi Active Berubah oleh Admin Lain Saat Modal Edit Dibuka atau Sedang Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, Andi Wijaya, env `Spectra.env.AC_TC_PASSWORD`), login di hook `before`; hook `after` mengembalikan sesi ke akun default suite yang sama.
- Dataset Riwayat A (Version 3 Active/John Doe 10 Aug 2026, Version 2, Version 1) di-seed di hook `before` lewat Fixture BE dan dikembalikan di hook `after`. Karena riwayat versi append-only dan setiap TC membuat `Version 4`, dataset dikembalikan ke Riwayat A lewat Fixture BE di antara TC (langkah penghubung).
- Kemampuan teknis: Fixture API "admin lain mem-publish `Version 4`" dengan konten yang berbeda dari Version 3 (dipakai TC-AC-PP-47, 48, 95), dipanggil tanpa me-refresh halaman user; tidak memakai browser kedua (pemicu bukan objek uji).
- Suite berjalan serial (`parallel: false`) karena spec mem-publish dan mengubah dokumen Privacy Policy yang bersifat tunggal platform-wide.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `kontenVersi4AdminLain` | Konten `Version 4` yang di-publish admin lain (berbeda dari Version 3) | TC-AC-PP-47, TC-AC-PP-48, TC-AC-PP-95 |

## Test Steps

### TC-AC-PP-47: Row action Edit memuat konten Active terbaru walau baris yang diklik sudah tidak Active

1. Buka Settings > Privacy Policy dan pastikan tabel menampilkan `Version 3` Active
2. Melalui Fixture API, admin lain mem-publish `Version 4` (tanpa me-refresh halaman user)
3. Klik `[⋯]` pada baris `Version 3`
4. Pilih `Edit`
5. Tunggu konten termuat
6. Verifikasi Title modal "Edit Privacy Policy"
7. Verifikasi info bar menampilkan `Version 4`
8. Verifikasi editor terisi konten Version 4 (`kontenVersi4AdminLain`), bukan konten Version 3
9. Klik `[✕]` (tanpa mengubah konten)
10. Verifikasi modal tertutup
11. Verifikasi tidak ada dialog yang tampil
12. Verifikasi tabel Version History ter-refresh menampilkan `Version 4` dengan badge `Active`
13. Kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang halaman

### TC-AC-PP-48: Tombol [Edit] di footer Modal View mengambil ulang konten Active terbaru dan info bar memakai versi terbaru

14. Klik teks tautan `Version 3`
15. Verifikasi Modal View `Version 3` terbuka
16. Melalui Fixture API, admin lain mem-publish `Version 4`
17. Klik `[Edit]` di footer Modal View
18. Tunggu konten termuat
19. Verifikasi info bar menampilkan `Version 4`
20. Verifikasi editor terisi konten Version 4 (`kontenVersi4AdminLain`), bukan konten yang tadi ditampilkan di state View
21. Klik `[✕]` tanpa mengubah konten
22. Verifikasi modal kembali ke state View yang menampilkan versi yang dibuka pada titik masuk: info bar `Version 3`
23. Verifikasi state View menampilkan konten `Version 3`
24. Verifikasi footer `[Edit]` tetap tampil (status baris saat dibuka)
25. Klik `[✕]` pada Modal View
26. Verifikasi tabel Version History ter-refresh menampilkan `Version 4` dengan badge `Active`
27. Kembalikan dataset ke Riwayat A lewat Fixture BE dan muat ulang halaman

### TC-AC-PP-95: Publish setelah versi Active berubah oleh admin lain saat state Edit terbuka

28. Klik `[⋯]` pada baris `Version 3`
29. Pilih `Edit`
30. Tunggu konten termuat
31. Klik di akhir konten
32. Ketik " Stale A."
33. Melalui Fixture API, admin lain mem-publish `Version 4` dengan konten berbeda
34. Klik `[Publish New Version]`
35. Klik `[Publish]` pada Dialog Publish Confirm
36. Verifikasi toast sukses "Success, Privacy Policy has been published."
37. Verifikasi Dialog Publish Confirm tertutup
38. Verifikasi modal tertutup
39. Verifikasi tidak ada dialog konflik
40. Verifikasi tabel menampilkan `Version 5` dengan badge `Active`
41. Klik teks tautan `Version 5`
42. Verifikasi konten `Version 5` adalah konten Version 3 ditambah " Stale A."
43. Klik `[✕]` pada Modal View
44. Klik teks tautan `Version 4`
45. Verifikasi `Version 4` dari admin lain tetap ada dan kontennya `kontenVersi4AdminLain` tidak berubah
46. Klik `[✕]` pada Modal View

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- P-2 (pemicu bukan objek uji): "admin lain mem-publish `Version 4`" dilakukan lewat Fixture API seperti yang ditulis TC, bukan sesi browser kedua; hanya berfungsi sebagai pemicu perubahan versi Active dan bukan objek asersi. Perilaku dua admin yang menekan `[Publish]` bersamaan ada di spec konkurensi `TC-AC-PP-E2E-055`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 13 dan 27 (reset dataset ke Riwayat A lewat Fixture BE lalu muat ulang) karena TC-AC-PP-47, 48, dan 95 sama-sama memulai dari Version 3 Active dan menghasilkan `Version 4`; langkah 43 dan 46 (menutup Modal View bersih lewat `[✕]`).
- Langkah 41-46 (membuka `Version 5` dan `Version 4` di Modal View) adalah aksi observasi yang diperlukan untuk Expected b dan c TC-AC-PP-95 ("berisi konten ..." dan "tetap ada dan tidak berubah").
- Spec melewati sekitar 35 langkah (46 langkah) tanpa pengecualian P-1/P-2/P-3 selain P-2 di atas; tidak dipecah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01), seluruh TC memakai satu dataset (Riwayat A) dan akun yang sama, tidak ada kelas harness lain, dan tiap blok `###` berdiri sendiri karena dataset dikembalikan ke Riwayat A di antara TC sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA: (1) TC-AC-PP-47, 48, dan 95 menyebut admin lain mem-publish `Version 4` "dengan konten berbeda" tanpa menyebut isinya; spec memakai fixture `kontenVersi4AdminLain` yang ditentukan tim FE. (2) TC-AC-PP-47 Expected a menyebut "konten Version 4 (bukan konten Version 3)" tanpa teks pembeda; asersi memakai nilai fixture. (3) Post Condition TC-AC-PP-47 dan 48 ("Tidak ada perubahan data oleh aktor TC ini") serta TC-AC-PP-95 (record audit per versi) tidak punya langkah observasi sehingga tidak diasersi.
