---
id: TC-AC-LA-E2E-062-resubmit-alur-utama
title: "Resubmit: Form Pre-filled, Record Baru, Snapshot Harga Baru, Stay on Form, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-229
  - TC-AC-LA-239
  - TC-AC-LA-230
  - TC-AC-LA-232
  - TC-AC-LA-488
  - TC-AC-LA-231
  - TC-AC-LA-240
  - TC-AC-LA-237
coverage:
  web: automated
---

# Resubmit: Form Pre-filled, Record Baru, Snapshot Harga Baru, Stay on Form, dan Klik Ganda

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (Pre-setup #4, Distributor PT Maju Bersama, Manage allocation Create+Read+Update); halaman dibuka hook `beforeEach` suite (tab Current).
- Akun: `dewiFullLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; Subscription `SUBS-20260101-A1B2C`, End Date 31 Dec 2026), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34).
- Konfigurasi: Require Approval for Allocation ON (Pre-setup #38) untuk langkah 1 sampai 48 dan OFF (Pre-setup #39) untuk langkah 50 sampai 73. Hook `before` memastikan ON lewat fixture backend (disediakan tim FE/BE); langkah 49 mengubahnya ke OFF; hook `after` memulihkan nilai awal.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #48 dan #49 bersama): tujuh alokasi `Canceled` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, tampil di tab History:
  - `{idR1}`, `{idR3}`, `{idR4}`, `{idR5}`, `{idR6}`, `{idR7}`: `Canceled` manual (bentuk Pre-setup #48);
  - `{idR2}`: `Canceled` oleh Timeout Auto-Cancel (bentuk Pre-setup #49).
  - Allocation ID record baru hasil Resubmit dibaca lewat kemampuan baca state BE berdasarkan referensi ke Allocation ID asal; disebut `{idR1Baru}` dan `{idR7Baru}` pada langkah.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture toggle Require Approval, fixture harga (mengubah dan memulihkan Product Price Concurrent User), fixture waktu (jam server dan jam browser ke tanggal acuan 22 Dec 2026), intercept jaringan (`Spectra.intercept()`) untuk menahan respons submit 5 detik, menampilkan kolom Cost pada List lewat Setup Column (pemulihan preferensi kolom di hook `after`), serta kemampuan membaca state BE (Status, Reserve, entri Allocation Log, referensi record baru ke record asal, saldo kantong).
- State global: toggle Require Approval diubah pada langkah 49; Product Price diubah pada langkah 28 dan dipulihkan pada langkah 39; jam server dan jam browser diatur pada langkah 29 dan dipulihkan pada langkah 39; intercept dilepas pada langkah 46; hook `after` memulihkan semuanya sebagai cadangan. Saldo kantong dikembalikan oleh pembersihan record seed.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Resubmit dari Canceled manual (toggle ON)

1. Klik tab `History`
2. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
3. Ketik Search `{idR1}`, tekan Enter
4. Catat jumlah entri Allocation Log `{idR1}` sebagai baseline
5. Klik row action `Resubmit` pada baris Canceled milik sendiri
6. Verifikasi form berjudul `Allocate License`
7. Verifikasi form terisi Client `PT Sejahtera`, Target, Type `Concurrent User`, dan Quantity `5`
8. Verifikasi tombol footer `[Clear Field]` dan `[Submit]`
9. Klik `[Submit]`
10. Verifikasi toast sukses: "Success, license allocation has been resubmitted."
11. Klik tab `Current`
12. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
13. Ketik Search `{idR1Baru}`, tekan Enter
14. Verifikasi record baru dengan Allocation ID baru (berbeda dari `{idR1}`) tampil di tab Current
15. Verifikasi Status record baru `Waiting for Approval` (mengikuti toggle ON)
16. Klik row action `Allocation Log`
17. Verifikasi Allocation Log memuat entri `Allocation created by Dewi A` dengan baris `Resubmitted From: {idR1}`
18. Tutup modal Allocation Log
19. Verifikasi record asal `{idR1}` tidak berubah: Status tetap `Canceled`
20. Verifikasi log record asal `{idR1}` tidak berubah: jumlah entri Allocation Log sama dengan baseline

### Resubmit dari Canceled hasil Timeout Auto-Cancel

21. Klik tab `History`
22. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
23. Ketik Search `{idR2}`, tekan Enter
24. Klik row action `Resubmit` pada baris Canceled hasil Timeout
25. Klik `[Submit]`
26. Verifikasi toast sukses: "Success, license allocation has been resubmitted."
27. Verifikasi record baru terbentuk dan menunjuk `{idR2}`

### Snapshot harga dan hari prorata baru

28. Naikkan harga Concurrent User dari `$365` menjadi `$730` (fixture harga)
29. Atur jam server dan jam browser ke 22 Dec 2026 (fixture waktu)
30. Ganti isi kotak search dengan `{idR3}`, tekan Enter
31. Pastikan kolom Cost tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Cost, lalu klik `[Save]`
32. Catat Cost record asal `{idR3}` pada List sebagai baseline
33. Klik row action `Resubmit`
34. Verifikasi Cost pada section Payment dihitung dengan harga saat ini `$730`, bukan snapshot record asal
35. Verifikasi Cost pada section Payment dihitung dengan hari dari tanggal Submit ulang, bukan snapshot record asal
36. Klik `[Submit]`
37. Tunggu aksi selesai
38. Verifikasi record asal `{idR3}` tetap menampilkan Cost lama (sama dengan baseline)
39. Pulihkan harga Concurrent User ke `$365` dan jam server serta jam browser ke nilai awal

### Klik ganda Submit

40. Ganti isi kotak search dengan `{idR4}`, tekan Enter
41. Tahan respons submit selama 5 detik (intercept)
42. Klik row action `Resubmit`
43. Klik ganda cepat `[Submit]`
44. Verifikasi `[Submit]` loading setelah klik pertama
45. Verifikasi `[Submit]` disabled setelah klik pertama
46. Lepas tahanan respons
47. Verifikasi hanya satu request terkirim: tepat satu record baru berstatus `Waiting for Approval` yang menunjuk `{idR4}`
48. Verifikasi Reserve ditahan sekali (tidak ganda)

### Toggle OFF: Resubmit berulang, record langsung Completed, dan Stay on this form

49. Ubah Require Approval for Allocation menjadi OFF (fixture toggle)
50. Ganti isi kotak search dengan `{idR5}`, tekan Enter
51. Klik row action `Resubmit`
52. Klik `[Submit]`
53. Klik row action `Resubmit` pada baris Canceled `{idR5}` yang sama
54. Klik `[Submit]`
55. Verifikasi dua record baru dengan Allocation ID berbeda, keduanya menunjuk `{idR5}`
56. Verifikasi record Canceled `{idR5}` tidak berubah
57. Ganti isi kotak search dengan `{idR6}`, tekan Enter
58. Klik row action `Resubmit`
59. Klik `[Submit]`
60. Verifikasi record baru yang menunjuk `{idR6}` langsung `Completed` berstatus `Active`
61. Ganti isi kotak search dengan `{idR7}`, tekan Enter
62. Klik row action `Resubmit`
63. Centang `Stay on this form after submitting`
64. Klik `[Submit]`
65. Verifikasi toast sukses: "Success, license allocation has been resubmitted."
66. Verifikasi form tetap terbuka
67. Verifikasi Client `PT Sejahtera` dipertahankan
68. Verifikasi Target dipertahankan
69. Klik `[×]`
70. Klik tab `Current`
71. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
72. Ketik Search `{idR7Baru}`, tekan Enter
73. Verifikasi List diperbarui: baris `{idR7Baru}` tampil

## Notes

- Alasan di atas sekitar 35 langkah: kedelapan TC satu topik (Resubmit dari record Canceled milik Dewi Anggraini pada form dan Client yang sama), kelas harness fungsional yang sama, tiap blok memakai record Canceled milik sendiri sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan blok berbeda dari urutan TC: semua blok toggle ON (TC-AC-LA-229, 239, 230, 232, 488) lebih dulu, lalu blok toggle OFF (TC-AC-LA-231, 240, 237), supaya toggle hanya diubah sekali (langkah 49). TC-AC-LA-239 dijalankan sebagai langkah 16 sampai 18 dan 20 di atas record hasil TC-AC-LA-229 (Dependensi TC-AC-LA-229).
- Langkah penghubung (S-03, R-16): langkah 2, 12, 22, 71 (mengosongkan kotak search lewat `✕` dan Enter sesudah pindah tab sebelum Search berikutnya; isi kotak setelah pindah tab tidak diandaikan), langkah 31 (menampilkan kolom Cost lewat Setup Column, tanpa `Verifikasi`; kolom Cost tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii), langkah 37 (menunggu aksi selesai sebelum memulihkan harga dan jam), langkah 3, 13, 23, 30, 40, 50, 57, 61, dan 72 (Search untuk menemukan baris), langkah 1, 11, 21, dan 70 (pindah tab), langkah 18 (menutup modal Allocation Log), langkah 32 (baseline Cost), langkah 39 (memulihkan harga dan jam), langkah 49 (mengubah toggle), langkah 69 (menutup form Resubmit).
- Langkah 41 sampai 46: respons ditahan sehingga toast belum muncul; spec tidak mengasersi toast pada TC-AC-LA-488 karena Expected tidak memuatnya.
- Temuan untuk QA:
  - TC-AC-LA-229 butir c, TC-AC-LA-231 butir a, TC-AC-LA-230 butir a, TC-AC-LA-240 butir a, dan TC-AC-LA-488 butir b menyebut "record baru" tanpa menyebut cara mengenali Allocation ID baru; spec memakai kemampuan baca state BE yang disediakan tim FE/BE (referensi ke Allocation ID asal) lalu mencarinya lewat Search.
  - TC-AC-LA-229 butir d, TC-AC-LA-231 butir b, dan TC-AC-LA-239 butir b ("record asal tidak berubah", "log tidak berubah") tidak menyebut cara mengamati; spec memakai Status baris dan jumlah entri Allocation Log dengan baseline.
  - TC-AC-LA-232 tidak menyebut nilai Cost yang diharapkan pada Expected (hanya "harga saat ini `$730` dan hari dari tanggal Submit ulang") dan tidak menyebut nilai Cost lama record asal; spec mengasersi dasar perhitungan dan membandingkan Cost asal dengan baseline.
  - TC-AC-LA-237 tidak menyebut keadaan pristine atau dirty form Resubmit sesudah Stay on this form; spec menutup form lewat `[×]` (langkah 69) tanpa dialog, sama dengan perilaku form Allocate pada TC-AC-LA-185.
  - TC-AC-LA-237 butir b ("List diperbarui") tidak menyebut tab yang diamati; spec membuka tab Current karena record baru dengan toggle OFF berstatus Active.
  - TC-AC-LA-240 dan TC-AC-LA-488 tidak menyebut kolom tempat Status dan Reserve dibaca; spec memakai kemampuan baca state BE untuk keduanya.
