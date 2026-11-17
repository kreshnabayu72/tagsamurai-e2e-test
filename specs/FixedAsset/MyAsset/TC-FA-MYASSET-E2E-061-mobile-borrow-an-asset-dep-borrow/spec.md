---
id: TC-FA-MYASSET-E2E-061-mobile-borrow-an-asset-dep-borrow
title: "Mobile: tombol Borrow an Asset, pinjam sendiri, dan pinjam atas nama lewat Borrow for"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§1.2#r43", "§2.1#r11", "§2.2#b1", "§3#p15", "§4.1b#p1", "§4.2.4#p1", "§4.3#r4", "§4.4#r12", "§4.6#p1", "§4.8#r10", "§7.3#r4", "§9.6#r7", "§9.7#r17"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r43": 22
  "§2.1#r11": [2, 22]
  "§2.2#b1": [12, 16]
  "§3#p15": 4
  "§4.1b#p1": [2, 16, 30, 32, 34]
  "§4.2.4#p1": [5, 7, 14]
  "§4.3#r4": 34
  "§4.4#r12": 4
  "§4.6#p1": [2, 22]
  "§4.8#r10": [2, 22]
  "§7.3#r4": [12, 27]
  "§9.6#r7": [16, 19, 20, 30, 32]
  "§9.7#r17": [16, 30, 32]
anchor: [33]
coverage:
  android: automated
---
# Mobile: tombol Borrow an Asset, pinjam sendiri, dan pinjam atas nama lewat Borrow for

## Prerequisites
- Aktor: Borrower yang juga PIC dari satu Borrower tanpa akun, karyawan aktif ber-akun login dengan role Read Only dan cakupan Group `Head Office`.
- Layar awal: halaman `My Asset` tab Task di aplikasi Android.
- Data:
  - DU-061-1: aset self-service `Projector Epson EB-X06 {runId}`, Group `Branch Surabaya`, Status `Available`, Self service efektif ON, Allowed borrower mencakup aktor. Group aset itu di luar cakupan Group role aktor.
  - DU-061-2: Borrower tanpa akun `Wulan Pratama {runId}`, PIC-nya adalah aktor.
  - DU-061-3: aset self-service `Meeting Mic Set {runId}`, Group `Head Office`, Status `Available`, Self service efektif ON, Allowed borrower mencakup `Wulan Pratama {runId}` dan tidak mencakup aktor.
  - DU-061-4: aset self-service `Flip Chart Stand {runId}`, Group `Head Office`, Status `Available`, Self service efektif ON, Allowed borrower mencakup `Wulan Pratama {runId}` dan tidak mencakup aktor.
  - Selain DU-061-1, DU-061-3, dan DU-061-4, tidak ada aset lain yang layak dipinjam aktor sendiri atau untuk Borrower tanpa akun DU-061-2.

## Test Steps

### Tombol Borrow an Asset tampil bagi Borrower dengan aset layak
1. Klik tab `Borrowed`
2. Verifikasi tombol `Borrow an Asset` tampil di tab Borrowed

### Halaman Borrow an Asset dibuka dan dibatalkan
3. Klik `Borrow an Asset`
4. Verifikasi halaman Borrow an Asset terbuka
5. Verifikasi breadcrumb `My Asset > Borrow an Asset` tampil
6. Klik `[Cancel]`
7. Verifikasi `My Asset` tab `Borrowed` tampil kembali

### Pinjam sendiri lewat Borrow Now
8. Klik `Borrow an Asset`
9. Pilih `Borrow for` `Me`
10. Pilih aset `Projector Epson EB-X06 {runId}`
11. Klik `Borrow Now`
12. Verifikasi panel hasil di halaman, bukan toast, memuat `Success, 1 asset is now borrowed. Return by [Date].`
13. Tutup panel hasil dan kembali ke `My Asset`
14. Verifikasi `My Asset` tab `Borrowed` tampil
15. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
16. Verifikasi kartu aset milik DU-061-1 tampil di tab Borrowed sebagai baris baru berstatus `Borrowed`
17. Klik menu ⋯ pada kartu aset milik DU-061-1
18. Klik `Borrow Log`
19. Verifikasi entri `Borrow requested` tampil di Borrow Log kartu aset milik DU-061-1
20. Verifikasi entri `Handed over` tampil di Borrow Log kartu aset milik DU-061-1
21. Tutup dialog Borrow Log

### Pinjam atas nama Borrower tanpa akun lewat Borrow for
22. Verifikasi tombol `Borrow an Asset` tetap tampil untuk aset milik DU-061-3 dan DU-061-4
23. Klik `Borrow an Asset`
24. Pilih `Borrow for` `Wulan Pratama {runId}`
25. Pilih aset `Meeting Mic Set {runId}` dan `Flip Chart Stand {runId}`
26. Klik `Borrow Now`
27. Verifikasi panel hasil di halaman, bukan toast, memuat `Success, 2 assets are now borrowed. Return by [Date].`
28. Tutup panel hasil dan kembali ke `My Asset`
29. Ganti isi kotak search dengan `Meeting Mic Set {runId}`, tekan Enter
30. Verifikasi kartu aset milik DU-061-3 tampil di tab Borrowed sebagai baris baru berstatus `Borrowed`
31. Ganti isi kotak search dengan `Flip Chart Stand {runId}`, tekan Enter
32. Verifikasi kartu aset milik DU-061-4 tampil di tab Borrowed sebagai baris baru berstatus `Borrowed`

### Tombol Borrow an Asset tidak tampil tanpa aset layak
33. Verifikasi ikon `Search` tampil pada toolbar tab Borrowed
34. Verifikasi tombol `Borrow an Asset` tidak tampil (Hidden) di tab Borrowed
