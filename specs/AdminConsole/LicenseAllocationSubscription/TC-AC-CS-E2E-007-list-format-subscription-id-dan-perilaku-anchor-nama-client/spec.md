---
id: TC-AC-CS-E2E-007-list-format-subscription-id-dan-perilaku-anchor-nama-client
title: "List: Format Subscription ID dan Perilaku Anchor Nama Client"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-24
  - TC-AC-CS-565
  - TC-AC-CS-566
  - TC-AC-CS-567
coverage:
  web: automated
---

# List: Format Subscription ID dan Perilaku Anchor Nama Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data: Client `Client Tanpa Subscription` (#48) tanpa term live untuk Product `FAMS`, `SAMS`, dan `SIEM`; ID `SUBS-20260819-00001` sampai `SUBS-20260819-00006` sudah dipakai fixture (#49, #57, #67, #59, #63, #90); Client `PT Sejahtera` dengan baris `SUBS-20260101-00001` (#61, baca-saja); Client `PT Pengelola Distribusi Perdagangan dan Jasa Nusantara Sejahtera Makmur Abadi Indonesia` dengan term SAMS Growth Active (#86, baca-saja).
- Kemampuan teknis: fixture waktu untuk mengatur jam server dan jam browser absolut ke `19/08/26` lalu `20/08/26` (tanggal acuan uji #28). Tiga term yang dibuat TC-AC-CS-24 dihapus dan jam dipulihkan oleh fixture backend di hook `after` (state Pre-setup #48 dan penghitung nomor urut ID dipulihkan; disediakan tim FE/BE, dicatat di `suite.md`). Efek pada Pre-setup #48: Last Updated dan entri audit trail Client Subscription berubah.
- Toggle Require Approval for Allocation tidak diubah; aktor Total Control Principal membuat term langsung berstatus Active.

## Test Steps

### TC-AC-CS-24: Format Subscription ID SUBS-YYYYMMDD-XXXXX

1. Atur jam server dan jam browser ke `19/08/26` melalui fixture waktu
2. Klik `[+ Subscription]`
3. Isi Client `Client Tanpa Subscription`, Product `FAMS`, Plan `Professional`, Duration `1`, Start Date `19/08/26`
4. Klik `[Submit]`
5. Tunggu aksi selesai (dialog/modal tertutup)
6. Klik `[+ Subscription]`
7. Isi Client `Client Tanpa Subscription`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
8. Klik `[Submit]`
9. Tunggu aksi selesai (dialog/modal tertutup)
10. Atur jam server dan jam browser ke `20/08/26` melalui fixture waktu
11. Klik `[+ Subscription]`
12. Isi Client `Client Tanpa Subscription`, Product `SIEM`, Plan `SIEM`, Duration `1`, Start Date `20/08/26`
13. Klik `[Submit]`
14. Tunggu aksi selesai (dialog/modal tertutup)
15. Ketik Search `Client Tanpa Subscription`, tekan Enter
16. Verifikasi setiap Subscription ID berformat `SUBS-YYYYMMDD-XXXXX` dengan sufiks lima digit desimal; bagian tanggal dua ID pertama `20260819` dan ID ketiga `20260820`
17. Verifikasi dua term pada hari yang sama bernomor berurutan: `SUBS-20260819-00007` lalu `SUBS-20260819-00008`
18. Verifikasi term pada tanggal berbeda mulai lagi dari `00001`: `SUBS-20260820-00001`
19. Pulihkan jam server dan jam browser melalui fixture waktu
20. Klik `(←)` pada kotak Search

### TC-AC-CS-565: Nama Client adalah real anchor: buka tab baru lewat Ctrl+klik dan Enter lewat keyboard

21. Ketik Search `SUBS-20260101-00001`, tekan Enter
22. Periksa elemen nama Client `PT Sejahtera` pada baris `SUBS-20260101-00001`
23. Verifikasi nama Client berupa tautan dengan alamat tujuan halaman Client Detail `PT Sejahtera` (real anchor, bukan elemen yang hanya menangani klik)
24. Ctrl+klik nama Client
25. Verifikasi Client Detail `PT Sejahtera` terbuka di tab baru
26. Verifikasi List tetap di tab asal
27. Tutup tab baru dan kembali ke tab asal
28. Fokus ke nama Client lewat tombol `Tab` lalu tekan `Enter`
29. Verifikasi Client Detail `PT Sejahtera` terbuka di tab yang sama
30. Klik tombol Back browser satu kali

### TC-AC-CS-566: Drag-select nama Client tidak menavigasi dan klik ganda cepat hanya menavigasi sekali

31. Ganti isi kotak search dengan `SUBS-20260101-00001`, tekan Enter
32. Tekan mouse di awal teks `PT Sejahtera`, seret ke akhir teks, lalu lepas
33. Verifikasi tidak ada navigasi dan halaman tetap List
34. Verifikasi teks `PT Sejahtera` terseleksi dan dapat disalin
35. Klik ganda cepat pada nama Client
36. Verifikasi Client Detail `PT Sejahtera` terbuka satu kali
37. Klik tombol Back browser satu kali
38. Verifikasi halaman sebelumnya adalah List dan tidak ada entri riwayat ganda

### TC-AC-CS-567: Nama Client panjang tampil utuh, header kolom tidak wrap, dan tinggi baris konsisten

39. Ganti isi kotak search dengan `Pengelola Distribusi`, tekan Enter
40. Verifikasi nama Client tampil utuh tanpa pemotongan `..` atau elipsis
41. Arahkan kursor ke nama Client panjang
42. Verifikasi tidak ada tooltip hover pada nama Client
43. Verifikasi kolom Client melebar mengikuti konten (hug content)
44. Verifikasi label semua header kolom tampil satu baris
45. Verifikasi baris dengan nama panjang tetap satu baris dengan tinggi sama seperti baris lain
46. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), `Klik (←)` pada kotak Search, tutup tab baru dan kembali ke tab asal pada TC-AC-CS-565, langkah `Tunggu aksi selesai (dialog/modal tertutup)` sesudah tiap `[Submit]` TC-AC-CS-24 (8b butir 8; mendahului pergeseran jam dan pembacaan List), serta langkah menggeser jam. Jam dipulihkan sebelum langkah Search dan asersi ID (jam tidak memengaruhi nilai ID yang sudah terbentuk).
- Cleanup: tiga term hasil TC-AC-CS-24 dihapus di hook `after` lewat fixture backend (lihat Prerequisites).
- Sesudah klik Back pada TC-AC-CS-565 dan TC-AC-CS-566, List dengan Search aktif ditampilkan lagi; Search diketik ulang pada blok berikutnya bila perlu (S-09).
- Spec ini 46 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (perilaku baris dan anchor nama Client pada List Subscriptions) dan berdiri sendiri; TC-AC-CS-24 butuh tiga kali pembuatan term lewat form sehingga tidak dapat dipersingkat.
- Temuan untuk QA:
  - TC-AC-CS-24 Expected b mengandalkan nomor `00001` sampai `00006` pada tanggal `19/08/26` sudah dipakai fixture dan tidak ada spec lain yang membuat term pada tanggal itu; suite serial dan fixture backend memulihkan penghitung nomor urut (kemampuan disediakan tim FE/BE; mekanisme tidak tertulis di TC, PRD, atau LLD).
  - TC-AC-CS-24 tidak menyebut toggle Require Approval for Allocation; spec mengandalkan aktor Principal sebagai bypass sehingga term langsung Active.
  - TC-AC-CS-565 menyebut cara memeriksa alamat tujuan elemen (real anchor) tanpa menyebut alat; kemampuan membaca atribut `href` elemen ditulis sebagai disediakan tim FE (S-11).
