---
id: TC-FA-FAAM-E2E-240-pencatatan-absence-tiga-surface-log
title: "Pencatatan Absence: Edit Tanpa Perubahan dan Cascade Tidak Menulis Entri di Tiga Surface Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-576
  - TC-FA-FAAM-577
coverage:
  web: automated
---

# Pencatatan Absence: Edit Tanpa Perubahan dan Cascade Tidak Menulis Entri di Tiga Surface Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup: No. 10 dan No. 10d (`Dell Latitude`, Total Asset 42, lisensi Tracking tersedia 30), No. 22 (Category `IT Equipment`, `Office Equipment`), No. 25 (Label `Finance`, `Fragile`).
- Data Dinamis, di-seed lewat API di hook `before`:
  - `Edit Target Item 576 {runId}-240` (Code `ETI576`): salinan fixture 13d, Total Asset 0, Category `IT Equipment`, TAG `QR`, Brand `Dell` model `5420`, UoM `Unit`.
  - `Dell Latitude` (fixture No. 10) tidak dapat digandakan dan menjadi target Edit TC-FA-FAAM-577. Hook `before` dan hook `after` menyediakannya ulang ke keadaan Pre-setup No. 10 dan No. 10d lewat seed API (kemampuan disediakan tim BE/FE). Efek pada Last Updated dan audit trail dicatat di sini: Last Updated `Dell Latitude` berubah oleh spec ini. Suite berjalan serial. Pernyataan ini belum ada di `suite.md` (lihat Temuan untuk QA).
- Kemampuan teknis: membuka Modal Changelog dan memakai Search di dalamnya; membaca jumlah entri Changelog (hasil Search), System Log (Detail User aktor, tab System Log), dan Activity Log FAMS sebelum dan sesudah aksi. Ketiganya adalah audit trail permanen sehingga hanya selisih terhadap baseline yang diasersi, bukan total absolut.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Edit Target Item 576 {runId}-240` lewat API dan sediakan ulang `Dell Latitude`.
- State global yang diubah: tidak ada (selain keadaan `Dell Latitude` di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-576 dan 577: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-576: Edit tanpa perubahan menulis nol entri di Changelog, System Log, dan Activity Log

1. Ketik Search `Edit Target Item 576 {runId}-240`, tekan Enter
2. Catat Modified By dan Last Updated baris `Edit Target Item 576 {runId}-240`
3. Klik icon Changelog
4. Ketik Search `Edit Target Item 576 {runId}-240`, tekan Enter
5. Catat jumlah baris Changelog `Edit Target Item 576 {runId}-240` sebagai baseline C1
6. Tutup Modal Changelog
7. Buka Detail User aktor lalu tab System Log
8. Catat jumlah entri System Log sebagai baseline S1
9. Buka Activity Log FAMS
10. Catat jumlah entri Activity Log FAMS sebagai baseline A1
11. Buka Fixed Asset > Settings > Asset Master > Asset Name
12. Ketik Search `Edit Target Item 576 {runId}-240`, tekan Enter
13. Klik `⋯` baris `Edit Target Item 576 {runId}-240` lalu `Edit`
14. Klik `[Save]` tanpa perubahan
15. Klik icon Changelog
16. Ketik Search `Edit Target Item 576 {runId}-240`, tekan Enter
17. Verifikasi baris Changelog `Edit Target Item 576 {runId}-240` yang ada pada baseline tetap tampil
18. Verifikasi jumlah baris Changelog sama dengan baseline C1
19. Tutup Modal Changelog
20. Buka Detail User aktor lalu tab System Log
21. Verifikasi entri System Log tampil
22. Verifikasi jumlah entri System Log sama dengan baseline S1
23. Buka Activity Log FAMS
24. Verifikasi entri Activity Log FAMS tampil
25. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline A1
26. Buka Fixed Asset > Settings > Asset Master > Asset Name
27. Ketik Search `Edit Target Item 576 {runId}-240`, tekan Enter
28. Verifikasi Modified By dan Last Updated baris `Edit Target Item 576 {runId}-240` sama dengan nilai pada langkah 2

### TC-FA-FAAM-577: Cascade Category, Default Label, dan Default Addon tidak menulis baris log tambahan

29. Ketik Search `Dell Latitude`, tekan Enter
30. Klik icon Changelog
31. Ketik Search `Dell Latitude`, tekan Enter
32. Catat jumlah baris Changelog `Dell Latitude` sebagai baseline C2
33. Tutup Modal Changelog
34. Klik `⋯` baris `Dell Latitude` lalu `Edit`
35. Ubah Category menjadi `Office Equipment`
36. Ubah Default Label menjadi `Fragile`
37. Ubah Default Addon menjadi `Tracking`
38. Klik `[Save]`
39. Konfirmasi dialog dampak yang tampil untuk Category, Default Label, dan Default Addon
40. Klik icon Changelog
41. Ketik Search `Dell Latitude`, tekan Enter
42. Verifikasi tiga baris Edit baru dengan Field `Category`, `Default Label`, dan `Default Addon` pada Asset Name `Dell Latitude`
43. Verifikasi jumlah baris Changelog `Dell Latitude` sama dengan baseline C2 ditambah tiga (tidak ada baris tambahan akibat cascade)
44. Tutup Modal Changelog
45. Buka Activity Log FAMS
46. Verifikasi tiga baris Edit untuk Asset Name `Dell Latitude` tampil dengan Field `Category`, `Default Label`, dan `Default Addon`
47. Verifikasi tidak ada baris log tingkat aset untuk 42 aset `Dell Latitude` (tidak ada baris Activity Log dengan Object selain `Asset Name` yang merujuk `Dell Latitude`)

## Notes

- P-5(a): spec ini kelas g; tidak ada pemicu kelas lain. Aksi Edit pada TC-FA-FAAM-576 dan TC-FA-FAAM-577 hanya membentuk kondisi yang diasersi tidak tercatat; tiap TC punya baseline sendiri.
- Di atas smell 35 langkah. Spec berisi 47 langkah, di atas ~35. Alasan: kedua blok kelas g, tiap blok berdiri sendiri dengan baseline sendiri, dan blok TC-FA-FAAM-576 membaca tiga surface log berbeda yang masing-masing memerlukan navigasi; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 12, 27, 29 (Search tabel utama), langkah 3 sampai 6, 15, 16, 30 sampai 33, 40, 41 (membuka dan mencari di Modal Changelog; S-12, S-14), langkah 7 sampai 11, 20, 23, 26, 45 (navigasi antar surface log), dan langkah 2, 5, 8, 10, 32 (mencatat baseline).
- Anchor positif absence: langkah 17, 21, 24 (entri pembanding tampil pada tiap surface) untuk langkah 18, 22, 25; langkah 42 dan 46 (tiga baris Edit tampil) untuk langkah 43 dan 47.
- Temuan untuk QA:
  - TC-FA-FAAM-576 memakai `Edit Target Item` literal; Tabel Data Uji Dinamis tidak memuat salinan untuk TC ini, sehingga spec memakai salinan `Edit Target Item 576` (Code `ETI576`).
  - TC-FA-FAAM-577 mengubah `Dell Latitude` (fixture tidak dapat digandakan). S-06 mensyaratkan pemulihan lewat fixture backend yang dinyatakan di `suite.md`; `suite.md` belum menyebutnya.
  - TC-FA-FAAM-577 tidak menyebut nilai Default Label dan Default Addon baru, dan tidak menyebut tombol pada dialog dampak; spec memilih `Fragile` dan `Tracking` (lisensi Tracking tersedia 30 menurut Pre-setup No. 10d) dan menulis "Konfirmasi dialog dampak".
  - Langkah 47: Expected "tidak ada baris log tingkat aset" tidak mendefinisikan kolom yang diperiksa; spec memeriksa Object selain `Asset Name`.
