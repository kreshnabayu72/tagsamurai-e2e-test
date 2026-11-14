---
id: TC-FA-FATR-UI-070-header
title: "Header halaman: breadcrumb, Export rules, dan tombol Changelog"
layer: ui-client
priority: High
caseType: Positive
status: draft
sourceRules:
  - §4.1#r1
  - §4.1#p1
  - §7#r11
  - §9.2#b309
  - §9.2#b316
  - §9.2#b317
  - §9.2#b320
  - §9.2#b321
  - §9.2#b373
  - §9.2#b374
  - §9.4.2#r50
  - §9.4.2#r51
  - §9.4.4#r41
  - §9.4.4#r42
  - §9.6#r4
  - EB-TBL-11
smoke: []
dependsOn: []
trace:
  §4.1#r1: [2, 6, 7, 9]
  §4.1#p1: [3, 4]
  §7#r11: 26
  §9.2#b309: [12, 13]
  §9.2#b316: [15, 17]
  §9.2#b317: 18
  §9.2#b320: 21
  §9.2#b321: 23
  §9.2#b373: [21, 23]
  §9.2#b374: 26
  §9.4.2#r50: [21, 23]
  §9.4.2#r51: 26
  §9.4.4#r41: [21, 23]
  §9.4.4#r42: 27
  §9.6#r4: [26, 28, 31, 33]
  EB-TBL-11: [3, 4, 5]
anchor: []
coverage:
  web: automated
---

# Header halaman: breadcrumb, Export rules, dan tombol Changelog

## Prerequisites
- Aktor: Total Control.
- Layar awal: Header halaman pada halaman Transaction Settings.
- Komponen: Header halaman
- Data:
  - DU-070-1: Draft Company default pada All categories: Max duration tab Borrow diubah dari `14` menjadi `10` dan belum disimpan.
  - DU-070-2: Berkas Export rules `Transaction-Rules` dengan `5.001` baris, lebih dari batas `5.000` baris.
- Kondisi:
  - K1: node All categories terpilih, tanpa draft, Export rules menghasilkan berkas dengan jumlah baris di bawah batas dan berhasil.
  - K2: node All categories terpilih, ada draft yang belum disimpan memakai DU-070-1, Export rules berhasil.
  - K3: node All categories terpilih, Export rules menghasilkan berkas memakai DU-070-2 dan berkas belum siap sampai pengujian melepasnya.
  - K4: node All categories terpilih, Export rules gagal diunduh.
  - K5: node All categories terpilih, respons Export rules ditahan sampai pengujian melepasnya.

## Test Steps

### Jejak halaman dan tombol header
1. Tampilkan Header halaman dengan kondisi K1
2. Verifikasi jejak halaman `Settings > Transaction Settings` tampil
3. Verifikasi segmen pertama `Settings` berupa teks statis, bukan tautan
4. Verifikasi segmen terakhir `Transaction Settings` berupa halaman aktif
5. Verifikasi jejak dua segmen itu tidak memuat segmen yang dapat diklik
6. Verifikasi tombol `Export rules` tampil dengan gaya outline dan severity contrast
7. Verifikasi tombol Changelog tampil di header
8. Arahkan kursor ke tombol Changelog
9. Verifikasi nama fungsi `Changelog` tersampaikan saat kursor berada di tombol

### Export rules langsung mengunduh
10. Tampilkan Header halaman dengan kondisi K1
11. Klik `Export rules`
12. Verifikasi unduhan berkas `Transaction-Rules` dimulai langsung
13. Verifikasi tidak ada dialog yang terbuka setelah `Export rules` diklik

### Export rules saat ada draft
14. Tampilkan Header halaman dengan kondisi K2
15. Verifikasi tombol `Export rules` aktif walau draft belum disimpan
16. Klik `Export rules`
17. Verifikasi unduhan berkas `Transaction-Rules` dimulai walau draft belum disimpan
18. Verifikasi tidak ada peringatan atau dialog konfirmasi tentang draft

### Export rules lebih dari 5.000 baris
19. Tampilkan Header halaman dengan kondisi K3
20. Klik `Export rules`
21. Verifikasi layar loading tampil selama berkas belum siap
22. Lepaskan berkas sebagai siap
23. Verifikasi berkas `Transaction-Rules` langsung terunduh begitu siap tanpa klik tambahan

### Export rules gagal diunduh
24. Tampilkan Header halaman dengan kondisi K4
25. Klik `Export rules`
26. Verifikasi toast `Error, failed to download Transaction-Rules.` tampil
27. Verifikasi tidak ada berkas yang terunduh
28. Verifikasi tombol `Export rules` aktif kembali untuk percobaan ulang

### Klik ganda Export rules
29. Tampilkan Header halaman dengan kondisi K5
30. Klik `Export rules`
31. Verifikasi tombol `Export rules` menampilkan keadaan loading dan disabled selama respons belum diterima
32. Klik `Export rules` sekali lagi
33. Verifikasi jumlah permintaan Export rules yang terkirim setelah dua klik adalah satu
