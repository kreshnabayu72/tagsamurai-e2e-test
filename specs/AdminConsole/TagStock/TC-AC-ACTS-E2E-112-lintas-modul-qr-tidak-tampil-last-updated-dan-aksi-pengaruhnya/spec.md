---
id: TC-AC-ACTS-E2E-112-lintas-modul-qr-tidak-tampil-last-updated-dan-aksi-pengaruhnya
title: "Lintas Modul: QR Tidak Tampil di Stock List, Last Updated Naik setelah Mark Damaged/Missing, Waiting, Approve, Reject, Cancel, dan Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-698
  - TC-AC-ACTS-699
  - TC-AC-ACTS-700
coverage:
  web: automated
---

# Lintas Modul: QR Tidak Tampil di Stock List, Last Updated Naik setelah Mark Damaged/Missing, Waiting, Approve, Reject, Cancel, dan Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: TAG > Stock (Stock List, dibuka hook `beforeEach` suite).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12) dengan unit milik spec ini, disiapkan seeding fixture BE (disediakan tim FE/BE): unit Available untuk Activate TAG, dua unit untuk Combine, unit untuk Mark as Damaged/Missing, dan unit untuk lima aksi pada TC-AC-ACTS-700 (Waiting for Approval, Approve, Reject, Canceled, Delete). Modul TAG > QR berisi QR Client (sedikitnya satu QR ter-generate). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Pemicu lintas modul (Activate TAG oleh Client, Combine, Mark as Damaged/Missing lewat Audit, serta Waiting, Approve, Reject, Canceled, Delete) disediakan tim FE/BE lewat sesi API aktor atau fixture BE; TC tidak merinci langkahnya. Kemampuan baca Last Updated SKU, jumlah entri Activity Log (baseline, S-12), dan waktu entri Activity Log terbaru.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-698: QR tidak tampil sebagai baris di Stock List dan TAG > QR bukan eager

1. Buka TAG > Stock
2. Verifikasi Stock List memuat baris SKU lain (anchor)
3. Verifikasi tidak ada baris QR di Stock List
4. Buka TAG > QR
5. Verifikasi TAG > QR menampilkan Client yang sudah punya QR ter-generate dan tidak menampilkan Client tanpa QR

### TC-AC-ACTS-699: Last Updated naik setelah Mark as Damaged/Missing tetapi tidak setelah Activate TAG atau Combine

6. Buka TAG > Stock dan catat Last Updated SKU `RFID-ASSET-CORE-R5`
7. Aktivasi satu unit lewat Global Settings hingga tersimpan (sesi API aktor)
8. Combine dua unit hingga tersimpan (fixture BE)
9. Tunggu 5 detik tanpa memuat ulang halaman
10. Buka TAG > Stock
11. Verifikasi Last Updated SKU tidak berubah terhadap nilai yang dicatat pada langkah 6 setelah Activate TAG dan Combine
12. Catat baseline jumlah entri Activity Log (filter Object `TAG Stock`; kemampuan baca), lalu jalankan Audit yang menandai satu unit Damaged/Missing hingga tersimpan (pemicu disediakan tim FE/BE)
13. Buka Activity Log (filter Object `TAG Stock`)
14. Verifikasi jumlah entri Activity Log bertambah dari baseline (selisih dicatat)
15. Baca waktu `Date` himpunan baris teratas sebanyak selisih itu (urutan default `Date` terbaru)
16. Buka TAG > Stock
17. Verifikasi Last Updated SKU naik ke waktu `Date` himpunan baris teratas yang dibaca (toleransi satu menit)

### TC-AC-ACTS-700: Last Updated naik setelah Waiting, Approve, Reject, Cancel, dan Delete

18. Catat baseline jumlah entri Activity Log (filter Object `TAG Stock`), lalu jalankan aksi Waiting for Approval pada unit SKU `RFID-ASSET-CORE-R5` hingga tersimpan
19. Buka TAG > Stock dan Activity Log
20. Verifikasi jumlah entri Activity Log bertambah dari baseline (selisih dicatat)
21. Verifikasi Last Updated sama dengan waktu `Date` himpunan baris teratas sebanyak selisih itu (urutan default `Date` terbaru; toleransi satu menit) setelah aksi Waiting for Approval
22. Catat baseline jumlah entri Activity Log (filter Object `TAG Stock`), lalu jalankan aksi Approve hingga tersimpan
23. Buka TAG > Stock dan Activity Log
24. Verifikasi jumlah entri Activity Log bertambah dari baseline (selisih dicatat)
25. Verifikasi Last Updated sama dengan waktu `Date` himpunan baris teratas sebanyak selisih itu (urutan default `Date` terbaru; toleransi satu menit) setelah aksi Approve
26. Catat baseline jumlah entri Activity Log (filter Object `TAG Stock`), lalu jalankan aksi Reject hingga tersimpan
27. Buka TAG > Stock dan Activity Log
28. Verifikasi jumlah entri Activity Log bertambah dari baseline (selisih dicatat)
29. Verifikasi Last Updated sama dengan waktu `Date` himpunan baris teratas sebanyak selisih itu (urutan default `Date` terbaru; toleransi satu menit) setelah aksi Reject
30. Catat baseline jumlah entri Activity Log (filter Object `TAG Stock`), lalu jalankan aksi Canceled hingga tersimpan
31. Buka TAG > Stock dan Activity Log
32. Verifikasi jumlah entri Activity Log bertambah dari baseline (selisih dicatat)
33. Verifikasi Last Updated sama dengan waktu `Date` himpunan baris teratas sebanyak selisih itu (urutan default `Date` terbaru; toleransi satu menit) setelah aksi Canceled
34. Catat baseline jumlah entri Activity Log (filter Object `TAG Stock`), lalu jalankan aksi Delete pada unit hingga tersimpan
35. Buka TAG > Stock dan Activity Log
36. Verifikasi jumlah entri Activity Log bertambah dari baseline (selisih dicatat)
37. Verifikasi Last Updated sama dengan waktu `Date` himpunan baris teratas sebanyak selisih itu (urutan default `Date` terbaru; toleransi satu menit) setelah aksi Delete

## Notes

- Mode: FE+BE. Jam server dan jam browser sinkron untuk asersi Last Updated sama dengan waktu entri Activity Log (S-12, toleransi satu menit).
- Spec ini melewati sekitar 35 langkah (37 langkah); alasan: semua blok satu pokok (Last Updated SKU terhadap waktu entri Activity Log setelah aksi) dengan satu dataset unit, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; baseline dan selisih jumlah entri dicatat per aksi (S-12).
- Cara baca entri audit trail baru (S-12, S-14): jumlah entri dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-699 dan TC-AC-ACTS-700 yang dibandingkan adalah kolom `Date` himpunan baris teratas sebanyak selisih (satu aksi dapat menulis beberapa entri dalam menit yang sama) dengan Last Updated SKU.
- Langkah penghubung tanpa Verifikasi (S-03): mencatat nilai awal dan membuka layar baca. Pelaku yang hanya memicu aksi memakai sesi API aktor dan ditulis "hingga tersimpan" (R-20). Asersi Last Updated tidak berubah pada TC-AC-ACTS-699 didahului pencatatan nilai awal sebagai baseline (S-12) dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" (pilihan spec, bukan nilai TC atau PRD).
- Absence baris QR pada TC-AC-ACTS-698 didahului anchor positif (baris SKU lain tampil; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-699 menyebut "jalankan Audit yang menandai satu unit Damaged/Missing" tanpa langkah Audit (reader RFID/NFC diperlukan); spec menuliskannya sebagai pemicu disediakan tim FE/BE.
  - TC-AC-ACTS-698 menyebut "TAG > QR menampilkan Client hanya setelah ada minimal satu QR ter-generate" tanpa data uji; spec menuliskan seeding Client dengan dan tanpa QR.
  - TC-AC-ACTS-700 menyebut aksi Waiting, Approve, Reject, Canceled, Delete tanpa langkah konkret; spec menuliskannya sebagai pemicu disediakan tim FE/BE.
