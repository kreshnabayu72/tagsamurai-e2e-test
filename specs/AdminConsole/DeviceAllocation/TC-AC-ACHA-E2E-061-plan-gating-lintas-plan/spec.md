---
id: TC-AC-ACHA-E2E-061-plan-gating-lintas-plan
title: "Plan Gating: Modul Device Allocation Berperilaku Sama pada Plan Terendah dan Plan Tertinggi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-466
coverage:
  web: automated
---

# Plan Gating: Modul Device Allocation Berperilaku Sama pada Plan Terendah dan Plan Tertinggi

## Prerequisites

- Mode: FE+BE.
- Kelas harness h (state tenant: perubahan plan tier). Dua entitas Distributor pada plan berbeda dibaca apa adanya (Pre-setup #67); spec tidak mengubah plan.
- Akun (Pre-setup #67, dua entitas Distributor pada plan berbeda masing-masing dengan akun Total Control dan kantong bersaldo cukup). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE:

| Akun | Entitas | Plan | Env var password |
|---|---|---|---|
| Total Control entitas plan terendah | Distributor plan terendah (Plans & Licensing > Plans & Features) | Plan terendah | `Spectra.env.AC_DA_TC_PLANLOW_PASSWORD` |
| Total Control entitas plan tertinggi | Distributor plan tertinggi (Plans & Licensing > Plans & Features) | Plan tertinggi | `Spectra.env.AC_DA_TC_PLANHIGH_PASSWORD` |

- Login akun pertama (Total Control entitas plan terendah) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column. Flag harus disetel untuk kedua akun di atas (pengecualian atas akun aktor default suite; disediakan tim FE).
- Data Pre-setup: #14 harga produk, Client binaan langsung masing-masing entitas (Client Active tidak tertulis di Pre-setup #67; lihat Temuan untuk QA) dan kantong masing-masing entitas bersaldo cukup (Pre-setup #67). Data yang dibuat spec: satu transaksi Completed pada tiap entitas (Category `TAG - BLE`, Quantity `5`). Data seeding milik spec (fixture seed per entitas, Precondition d TC-AC-ACHA-466; fixture API disediakan tim FE/BE): satu transaksi Waiting for Approval dan satu transaksi Canceled milik akun Total Control tiap entitas; Allocation ID keduanya ditangkap dari respons fixture seeding (Dynamic Reference) dan dipakai sebagai penanda Search dan cleanup hook `after`.
- Kemampuan teknis: mendeteksi berkas CSV terunduh (isi berkas tidak dibaca); hook `before` memastikan plan kedua entitas berbeda lewat fixture baca (disediakan tim FE/BE), tanpa langkah asersi.
- Pemulihan dan efek (R-08, S-06): transaksi Completed tidak dapat dihapus (modul tidak punya Delete); efek spec pada saldo kantong dan kuota Client kedua entitas (satu alokasi Quantity 5 per entitas) dipulihkan hook `after` lewat fixture yang disediakan tim FE/BE; transaksi hasil Resubmit yang tetap Waiting for Approval dibatalkan dan seed dipulihkan lewat fixture yang sama.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Plan terendah

1. Buka Allocation > Device Allocation
2. Verifikasi menu Allocation > Device Allocation tersedia pada entitas plan terendah
3. Klik `[+ Allocation]`
4. Verifikasi form Allocate Device tampil
5. Verifikasi tidak ada ikon kunci pada form
6. Pilih Category `TAG - BLE`, Client binaan langsung entitas, dan isi Quantity `5`
7. Klik `[Submit]` jalur langsung
8. Verifikasi toast sukses "Success, device allocation has been created."
9. Ketik Search Allocation ID transaksi Waiting for Approval milik akun Total Control entitas plan terendah (fixture seed per entitas), tekan Enter
10. Klik `Edit` pada transaksi itu, ubah Quantity menjadi `6`, lalu klik `[Save]`
11. Verifikasi toast sukses "Success, device allocation has been updated."
12. Klik `Cancel Allocation` pada transaksi yang sama, lalu konfirmasi di dialog
13. Verifikasi toast sukses "Success, device allocation has been canceled."
14. Verifikasi status transaksi itu `Canceled`
15. Ganti isi kotak search dengan Allocation ID transaksi Canceled milik akun Total Control entitas plan terendah (fixture seed per entitas), tekan Enter
16. Klik `Resubmit` pada transaksi itu, lalu klik `[Submit]`
17. Verifikasi toast sukses "Success, device allocation has been resubmitted."
18. Klik Download lalu `Download as CSV`
19. Verifikasi berkas CSV terunduh
20. Verifikasi tidak ada ikon kunci pada menu dan Table Tools
21. Verifikasi tidak ada banner upgrade dan tidak ada penolakan karena plan

### Ganti akun ke plan tertinggi

22. Logout lalu login sebagai Total Control entitas plan tertinggi, lalu buka Allocation > Device Allocation

### Plan tertinggi

23. Verifikasi menu Allocation > Device Allocation tersedia pada entitas plan tertinggi
24. Klik `[+ Allocation]`
25. Verifikasi form Allocate Device tampil
26. Verifikasi tidak ada ikon kunci pada form
27. Pilih Category `TAG - BLE`, Client binaan langsung entitas, dan isi Quantity `5`
28. Klik `[Submit]` jalur langsung
29. Verifikasi toast sukses "Success, device allocation has been created."
30. Ketik Search Allocation ID transaksi Waiting for Approval milik akun Total Control entitas plan tertinggi (fixture seed per entitas), tekan Enter
31. Klik `Edit` pada transaksi itu, ubah Quantity menjadi `6`, lalu klik `[Save]`
32. Verifikasi toast sukses "Success, device allocation has been updated."
33. Klik `Cancel Allocation` pada transaksi yang sama, lalu konfirmasi di dialog
34. Verifikasi toast sukses "Success, device allocation has been canceled."
35. Verifikasi status transaksi itu `Canceled`
36. Ganti isi kotak search dengan Allocation ID transaksi Canceled milik akun Total Control entitas plan tertinggi (fixture seed per entitas), tekan Enter
37. Klik `Resubmit` pada transaksi itu, lalu klik `[Submit]`
38. Verifikasi toast sukses "Success, device allocation has been resubmitted."
39. Klik Download lalu `Download as CSV`
40. Verifikasi berkas CSV terunduh
41. Verifikasi tidak ada ikon kunci pada menu dan Table Tools
42. Verifikasi tidak ada banner upgrade dan tidak ada penolakan karena plan

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 9c, TC-AC-ACHA-466). Subjudul `###` memetakan langkah ke id TC granular.
- Kelas h (perubahan plan tier) satu spec sendiri; spec membaca dua entitas yang sudah berada di plan berbeda dan tidak mengubah plan.
- Langkah penghubung (S-03): langkah ganti akun (S-07) dan langkah membuka halaman.
- Baris target (R-16): transaksi Waiting for Approval ditemukan lewat Search Allocation ID fixture seed (langkah 9 dan 30), transaksi Canceled lewat "ganti isi kotak search" dengan Allocation ID fixture seed; Search diketik sebagai langkah penghubung sebelum aksi baris.
- Asersi tambahan (S-03): `Verifikasi` toast sukses Edit, Cancel, dan Resubmit memakai teks toast spec 026, 029, dan 031 (TC-AC-ACHA-466 tidak menyebut teks toast) sebagai bukti aksi tersimpan; `Verifikasi` tidak ada ikon kunci pada form ditaruh sesudah form tampil (langkah 5 dan 26), bukan sesudah form tertutup.
- Ukuran spec: 42 langkah (melewati sekitar 35 langkah). Alasan: dua blok identik satu topik (plan terendah dan plan tertinggi) dengan satu dataset; tiap aksi TC-AC-ACHA-466 (Allocate, Edit, Cancel, Resubmit, Download) mempunyai `Verifikasi` sendiri (S-01) dan ganti akun menambah langkah tanpa verifikasi.
- Asersi absence (ikon kunci, banner upgrade, penolakan): didahului `Verifikasi` yang membuktikan sesuatu pada halaman yang sama tampil (form tampil, toast sukses, berkas terunduh), sehingga hasil kosong bukan karena halaman belum termuat (bagian 8b butir 2).
- Pengecualian S-12 nama literal: tidak ada.
- Temuan untuk QA:
  - TC-AC-ACHA-466 Precondition d menyebut satu transaksi Waiting for Approval dan satu transaksi Canceled per entitas tanpa Allocation ID, Quantity, atau Category; spec menangkap Allocation ID dari respons fixture seeding dan memakai Quantity Edit `6` sebagai pilihan spec.
  - Pre-setup #67 tidak menyebut email akun Total Control kedua entitas, nama entitas, nama Client binaan, atau nama kantong; spec memakai deskripsi peran dan menyebut data itu disediakan tim FE (S-11).
  - TC-AC-ACHA-466 tidak menyebut Category, Client, dan Quantity yang dipakai; spec memakai `TAG - BLE`, Client binaan langsung entitas, dan Quantity `5` sebagai pilihan spec.
  - TC-AC-ACHA-466 b ("modul tidak memiliki plan gating") tidak menyebut surface yang diamati untuk ikon kunci dan banner upgrade; spec mengamati menu, form, dan Table Tools.
  - Post Condition TC-AC-ACHA-466 ("Wallet Balance ... Client Dashboard ...") tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan.
