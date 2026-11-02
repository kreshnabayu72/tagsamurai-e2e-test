---
id: TC-FA-CAT-E2E-050-edit-clear-field-saving-state-move-tidak-didukung-refresh-dan-route-dirty
title: "Edit Category: Saving State, Clear Field, Move Tidak Didukung, serta Refresh F5 dan Pindah Route Saat Form Dirty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-171
  - TC-FA-CAT-172
  - TC-FA-CAT-203
  - TC-FA-CAT-620
  - TC-FA-CAT-621
coverage:
  web: automated
---

# Edit Category: Saving State, Clear Field, Move Tidak Didukung, serta Refresh F5 dan Pindah Route Saat Form Dirty

## Prerequisites

- Mode: FE+BE (backend nyata; penundaan respons Edit pada TC-FA-CAT-171 memakai `Spectra.intercept()` di atas backend nyata, dan state tersimpan diasersi lewat pembacaan state BE).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data milik spec (seed lewat API di hook `before`, disediakan tim FE/BE): kategori L1 leaf `Furniture {runId}-050` (Code `FURN050`, Total Asset 0) menjadi target Edit (S-06). Blok TC-FA-CAT-171 dan TC-FA-CAT-620 menyimpan perubahan (Description `Saving desc {runId}-050` dan Category Name `Unload Edit {runId}-050`). Pemulihan `Furniture {runId}-050` (Name, Code, Description) ke nilai seed lewat API dijalankan sebagai langkah penghubung sesudah tiap blok yang menyimpan; hook `after` menghapus kategori itu. Hook `before` juga membersihkan kategori ber-Code literal `FURN050` yang tersisa dari run sebelumnya sebelum seed. Data Pre-setup #20 tidak diubah (TC menyebut baris Furniture Pre-setup; spec memakai kategori milik spec setara). Efek: entri Changelog CatMain bertambah (audit trail permanen; tidak ada asersi jumlah); suite berjalan serial.
- Kemampuan teknis: dialog `beforeunload` browser dapat diamati dan dibatalkan atau dikonfirmasi dari spec (TC-FA-CAT-620); membaca state BE kategori `Furniture {runId}-050`; disediakan tim FE/BE.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Kebutuhan intercept (`Spectra.intercept()`): TC-FA-CAT-171 menunda respons Edit 3 detik; dilepas segera sesudah asersi state sementara.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-171: Tombol [Save] masuk saving state

1. Klik elipsis (⋯) pada baris `Furniture {runId}-050` > `Edit`
2. Ubah Description menjadi `Saving desc {runId}-050`
3. Tunda respons Edit 3 detik lewat intercept jaringan
4. Klik `[Save]`
5. Verifikasi `[Save]` menampilkan spinner
6. Verifikasi `[Save]` disabled
7. Verifikasi `[Clear Field]`, icon close (✕), dan input disabled sampai respons diterima
8. Lepas penundaan respons Edit
9. Verifikasi popup Edit tertutup
10. Verifikasi toast `Success, category has been updated.` tampil
11. Pulihkan `Furniture {runId}-050` ke nilai seed lewat API

### TC-FA-CAT-172: [Clear Field] popup Edit mengosongkan seluruh field

12. Klik elipsis (⋯) pada baris `Furniture {runId}-050` > `Edit`
13. Klik `[Clear Field]`
14. Verifikasi Category Name kosong
15. Verifikasi Category Code kosong
16. Verifikasi Description kosong
17. Verifikasi popup tetap terbuka
18. Verifikasi fokus berada di Category Name
19. Verifikasi dialog Unsaved Changes tidak tampil
20. Verifikasi data tersimpan `Furniture {runId}-050` belum berubah (dibaca dari state BE)
21. Klik icon close (✕)
22. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
23. Klik `[Leave]`

### TC-FA-CAT-203: Edit tidak menyediakan kontrol pindah parent

24. Klik elipsis (⋯) pada baris `Furniture {runId}-050` > `Edit`
25. Verifikasi popup Edit hanya memuat Category Name, Code, dan Description tanpa field parent
26. Klik icon close (✕)
27. Klik elipsis (⋯) pada baris `Furniture {runId}-050`
28. Verifikasi menu row action `Furniture {runId}-050` tampil
29. Verifikasi menu row action tidak memuat aksi `Move` atau `Reparent`
30. Verifikasi `Furniture {runId}-050` tetap berada sebagai kategori level 1 (posisi node tidak berubah)
31. Tekan `Esc` untuk menutup menu

### TC-FA-CAT-620: Refresh F5 saat popup Edit berubah

32. Klik elipsis (⋯) pada baris `Furniture {runId}-050` > `Edit`
33. Ubah Category Name menjadi `Unload Edit {runId}-050`
34. Tekan F5
35. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
36. Batalkan konfirmasi sehingga halaman tidak dimuat ulang
37. Klik `[Save]`
38. Tunggu popup Edit tertutup (penyimpanan selesai)
39. Klik elipsis (⋯) pada baris `Unload Edit {runId}-050` > `Edit` tanpa mengubah apa pun
40. Tekan F5
41. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser
42. Pulihkan `Furniture {runId}-050` ke nilai seed lewat API dan muat ulang halaman Categories

### TC-FA-CAT-621: Berpindah route SPA saat popup Edit berubah

43. Klik elipsis (⋯) pada baris `Furniture {runId}-050` > `Edit`
44. Ubah Category Name menjadi `Route Edit {runId}-050`
45. Klik link menu lain pada sidebar navigasi
46. Verifikasi perpindahan route dicegat dan dialog `You have unsaved changes. Are you sure you want to leave?` tampil
47. Klik `[Cancel]` pada dialog
48. Verifikasi navigasi dibatalkan: halaman tetap Categories dengan popup Edit terbuka
49. Verifikasi input Category Name `Route Edit {runId}-050` dipertahankan
50. Klik link menu lain pada sidebar navigasi lagi
51. Klik `[Leave]` pada dialog
52. Verifikasi navigasi dilanjutkan: halaman menu tujuan tampil
53. Verifikasi perubahan Category Name `Route Edit {runId}-050` tidak tersimpan (dibaca dari state BE)

## Notes

- Mode: FE+BE. Lima blok berdiri sendiri (perilaku popup Edit pada satu baris) sehingga jumlah langkah (53) melewati sekitar 35; kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (S-03, S-08, S-09): langkah 8 (melepas penundaan agar respons diterima), langkah 11 (memulihkan `Furniture {runId}-050`), langkah 42 (memulihkan `Furniture {runId}-050` lalu memuat ulang halaman Categories agar daftar memakai nama seed sebelum langkah 43), langkah 21 sampai 23 (menutup form dirty: ✕, dialog Unsaved Changes, `[Leave]`), langkah 26 (menutup popup yang bersih), langkah 27 dan 31 (membuka dan menutup menu row action), langkah 36 (membatalkan konfirmasi), langkah 38 (menunggu penyimpanan selesai sebelum membuka Edit lagi).
- Langkah 28 (menu row action tampil) adalah anchor positif untuk asersi absence langkah 29 (bagian 8b butir 2); tidak ada di Expected TC (S-03).
- Blok TC-FA-CAT-621 berakhir di halaman menu tujuan; hook `beforeEach` suite membuka Categories untuk spec berikutnya.
- Temuan untuk QA:
  - TC-FA-CAT-621 menyebut "link menu lain" pada sidebar tanpa menyebut menu tujuan; spec mengikuti TC dan tujuan ditetapkan saat script.
  - TC-FA-CAT-203 Expected b "posisi node tetap permanen" tidak punya langkah observasi spesifik; langkah 30 menafsirkannya sebagai node tetap di level 1.
  - TC-FA-CAT-171, 172, 203, 620, dan 621 menyebut baris `Furniture` Pre-setup sebagai target Edit; spec memakai kategori milik spec `Furniture {runId}-050` (S-06) agar data Pre-setup tidak berubah.
  - TC-FA-CAT-620 langkah 4 tidak menyebut asersi hasil Save; langkah 38 hanya menunggu penyimpanan selesai.
- Spec melewati 35 langkah (53 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri.
