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
- Konfigurasi: Require Approval for Allocation ON (Pre-setup #38) untuk langkah 1 sampai 39 dan OFF (Pre-setup #39) untuk langkah 41 sampai 61. Hook `before` memastikan ON lewat fixture backend (disediakan tim FE/BE); langkah 40 mengubahnya ke OFF; hook `after` memulihkan nilai awal.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #48 dan #49 bersama): tujuh alokasi `Canceled` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, tampil di tab History:
  - `{idR1}`, `{idR3}`, `{idR4}`, `{idR5}`, `{idR6}`, `{idR7}`: `Canceled` manual (bentuk Pre-setup #48);
  - `{idR2}`: `Canceled` oleh Timeout Auto-Cancel (bentuk Pre-setup #49).
  - Allocation ID record baru hasil Resubmit dibaca lewat kemampuan baca state BE berdasarkan referensi ke Allocation ID asal; disebut `{idR1Baru}` dan `{idR7Baru}` pada langkah.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture toggle Require Approval, fixture harga (mengubah dan memulihkan Product Price Concurrent User), fixture waktu (jam server dan jam browser ke tanggal acuan 22 Dec 2026), intercept jaringan (`Spectra.intercept()`) untuk menahan respons submit 5 detik, serta kemampuan membaca state BE (Status, Reserve, entri Allocation Log, referensi record baru ke record asal, saldo kantong).
- State global: toggle Require Approval diubah pada langkah 40; Product Price diubah pada langkah 23 dan dipulihkan pada langkah 31; jam server dan jam browser diatur pada langkah 24 dan dipulihkan pada langkah 31; intercept dilepas pada langkah 37; hook `after` memulihkan semuanya sebagai cadangan. Saldo kantong dikembalikan oleh pembersihan record seed.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Resubmit dari Canceled manual (toggle ON)

1. Klik tab `History`
2. Ketik Search `{idR1}`, tekan Enter
3. Catat jumlah entri Allocation Log `{idR1}` sebagai baseline
4. Klik row action `Resubmit` pada baris Canceled milik sendiri
5. Verifikasi form berjudul `Allocate License` terisi Client `PT Sejahtera`, Target, Type `Concurrent User`, dan Quantity `5`
6. Verifikasi tombol footer `[Clear Field]` dan `[Submit]`
7. Klik `[Submit]`
8. Verifikasi toast sukses: "Success, license allocation has been resubmitted."
9. Klik tab `Current`
10. Ketik Search `{idR1Baru}`, tekan Enter
11. Verifikasi record baru dengan Allocation ID baru (berbeda dari `{idR1}`) tampil di tab Current dengan Status `Waiting for Approval` (mengikuti toggle ON)
12. Klik row action `Allocation Log`
13. Verifikasi Allocation Log memuat entri `Allocation created by Dewi A` dengan baris `Resubmitted From: {idR1}`
14. Tutup modal Allocation Log
15. Verifikasi record asal `{idR1}` tidak berubah: Status tetap `Canceled`
16. Verifikasi log record asal `{idR1}` tidak berubah: jumlah entri Allocation Log sama dengan baseline

### Resubmit dari Canceled hasil Timeout Auto-Cancel

17. Klik tab `History`
18. Ketik Search `{idR2}`, tekan Enter
19. Klik row action `Resubmit` pada baris Canceled hasil Timeout
20. Klik `[Submit]`
21. Verifikasi toast sukses: "Success, license allocation has been resubmitted."
22. Verifikasi record baru terbentuk dan menunjuk `{idR2}`

### Snapshot harga dan hari prorata baru

23. Naikkan harga Concurrent User dari `$365` menjadi `$730` (fixture harga)
24. Atur jam server dan jam browser ke 22 Dec 2026 (fixture waktu)
25. Ganti isi kotak search dengan `{idR3}`, tekan Enter
26. Catat Cost record asal `{idR3}` pada List sebagai baseline
27. Klik row action `Resubmit`
28. Verifikasi Cost pada section Payment dihitung dengan harga saat ini `$730` dan hari dari tanggal Submit ulang, bukan snapshot record asal
29. Klik `[Submit]`
30. Verifikasi record asal `{idR3}` tetap menampilkan Cost lama (sama dengan baseline)
31. Pulihkan harga Concurrent User ke `$365` dan jam server serta jam browser ke nilai awal

### Klik ganda Submit

32. Ganti isi kotak search dengan `{idR4}`, tekan Enter
33. Tahan respons submit selama 5 detik (intercept)
34. Klik row action `Resubmit`
35. Klik ganda cepat `[Submit]`
36. Verifikasi `[Submit]` loading dan disabled setelah klik pertama
37. Lepas tahanan respons
38. Verifikasi hanya satu request terkirim: tepat satu record baru berstatus `Waiting for Approval` yang menunjuk `{idR4}`
39. Verifikasi Reserve ditahan sekali (tidak ganda)

### Toggle OFF: Resubmit berulang, record langsung Completed, dan Stay on this form

40. Ubah Require Approval for Allocation menjadi OFF (fixture toggle)
41. Ganti isi kotak search dengan `{idR5}`, tekan Enter
42. Klik row action `Resubmit`
43. Klik `[Submit]`
44. Klik row action `Resubmit` pada baris Canceled `{idR5}` yang sama
45. Klik `[Submit]`
46. Verifikasi dua record baru dengan Allocation ID berbeda, keduanya menunjuk `{idR5}`
47. Verifikasi record Canceled `{idR5}` tidak berubah
48. Ganti isi kotak search dengan `{idR6}`, tekan Enter
49. Klik row action `Resubmit`
50. Klik `[Submit]`
51. Verifikasi record baru yang menunjuk `{idR6}` langsung `Completed` berstatus `Active`
52. Ganti isi kotak search dengan `{idR7}`, tekan Enter
53. Klik row action `Resubmit`
54. Centang `Stay on this form after submitting`
55. Klik `[Submit]`
56. Verifikasi toast sukses: "Success, license allocation has been resubmitted."
57. Verifikasi form tetap terbuka dengan Client `PT Sejahtera` dan Target dipertahankan
58. Klik `[✕]`
59. Klik tab `Current`
60. Ketik Search `{idR7Baru}`, tekan Enter
61. Verifikasi List diperbarui: baris `{idR7Baru}` tampil

## Notes

- Alasan di atas sekitar 35 langkah: kedelapan TC satu topik (Resubmit dari record Canceled milik Dewi Anggraini pada form dan Client yang sama), kelas harness fungsional yang sama, tiap blok memakai record Canceled milik sendiri sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan blok berbeda dari urutan TC: semua blok toggle ON (TC-AC-LA-229, 239, 230, 232, 488) lebih dulu, lalu blok toggle OFF (TC-AC-LA-231, 240, 237), supaya toggle hanya diubah sekali (langkah 40). TC-AC-LA-239 dijalankan sebagai langkah 12 sampai 14 dan 16 di atas record hasil TC-AC-LA-229 (Dependensi TC-AC-LA-229).
- Langkah penghubung (S-03, R-16): langkah 2, 10, 18, 25, 32, 41, 48, 52, dan 60 (Search untuk menemukan baris), langkah 1, 9, 17, dan 59 (pindah tab), langkah 14 (menutup modal Allocation Log), langkah 26 (baseline Cost), langkah 31 (memulihkan harga dan jam), langkah 40 (mengubah toggle), langkah 58 (menutup form Resubmit).
- Langkah 33 sampai 37: respons ditahan sehingga toast belum muncul; spec tidak mengasersi toast pada TC-AC-LA-488 karena Expected tidak memuatnya.
- Temuan untuk QA:
  - TC-AC-LA-229 butir c, TC-AC-LA-231 butir a, TC-AC-LA-230 butir a, TC-AC-LA-240 butir a, dan TC-AC-LA-488 butir b menyebut "record baru" tanpa menyebut cara mengenali Allocation ID baru; spec memakai kemampuan baca state BE yang disediakan tim FE/BE (referensi ke Allocation ID asal) lalu mencarinya lewat Search.
  - TC-AC-LA-229 butir d, TC-AC-LA-231 butir b, dan TC-AC-LA-239 butir b ("record asal tidak berubah", "log tidak berubah") tidak menyebut cara mengamati; spec memakai Status baris dan jumlah entri Allocation Log dengan baseline.
  - TC-AC-LA-232 tidak menyebut nilai Cost yang diharapkan pada Expected (hanya "harga saat ini `$730` dan hari dari tanggal Submit ulang") dan tidak menyebut nilai Cost lama record asal; spec mengasersi dasar perhitungan dan membandingkan Cost asal dengan baseline.
  - TC-AC-LA-237 tidak menyebut keadaan pristine atau dirty form Resubmit sesudah Stay on this form; spec menutup form lewat `[✕]` (langkah 58) tanpa dialog, sama dengan perilaku form Allocate pada TC-AC-LA-185.
  - TC-AC-LA-237 butir b ("List diperbarui") tidak menyebut tab yang diamati; spec membuka tab Current karena record baru dengan toggle OFF berstatus Active.
  - TC-AC-LA-240 dan TC-AC-LA-488 tidak menyebut kolom tempat Status dan Reserve dibaca; spec memakai kemampuan baca state BE untuk keduanya.
