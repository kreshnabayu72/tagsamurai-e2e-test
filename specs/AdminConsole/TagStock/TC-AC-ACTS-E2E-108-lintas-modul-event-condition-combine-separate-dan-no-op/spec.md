---
id: TC-AC-ACTS-E2E-108-lintas-modul-event-condition-combine-separate-dan-no-op
title: "Lintas Modul: Event Condition Mengubah Status Tab In Use, Combine dan Separate, Event atau Delete TAG No-Op, dan Status Kembali Kosong setelah Delete TAG Jalur A"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-681
  - TC-AC-ACTS-682
  - TC-AC-ACTS-683
  - TC-AC-ACTS-684
  - TC-AC-ACTS-781
  - TC-AC-ACTS-782
coverage:
  web: automated
---

# Lintas Modul: Event Condition Mengubah Status Tab In Use, Combine dan Separate, Event atau Delete TAG No-Op, dan Status Kembali Kosong setelah Delete TAG Jalur A

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: TAG > Stock (Stock List, dibuka hook `beforeEach` suite).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12) dan `NFC-CARD-BETA-N2` (#13) dengan unit milik spec ini, disiapkan seeding fixture BE (disediakan tim FE/BE): unit In Use Status Available (TC-AC-ACTS-681), unit In Use Status Damaged/Missing (TC-AC-ACTS-682), unit RFID dan NFC Available untuk Combine (TC-AC-ACTS-683), set Combined aktif (TC-AC-ACTS-684), unit Available U1, unit Waiting for Approval non-collision U2, TAG Code unit yang sudah dihapus U3, dan TAG Code tak dikenal (TC-AC-ACTS-781), serta unit In Use hasil aktivasi Jalur A dengan Status Damaged/Missing (TC-AC-ACTS-782). Client memiliki akses Global Settings > TAG; event Condition, Delete TAG, dan Activate TAG dipicu lewat sesi API aktor (akun Client tidak ada di Pre-setup TC; disediakan tim FE/BE). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: kemampuan memicu Combine dan Separate di TAG > Combine & Separate (langkah UI modul itu tidak dirinci di TC), kemampuan baca status event (di-ack tanpa retry atau dead-letter), jumlah entri Activity Log, jumlah unit SKU, Status dan Condition unit, serta Last Updated SKU sebagai baseline (S-12). Jendela "Tunggu 5 detik tanpa memuat ulang halaman" untuk asersi tidak berubah adalah pilihan spec (bukan nilai TC atau PRD). State unit dipulihkan lewat fixture BE di hook `after`.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-681: Event Condition Damaged/Missing mengubah kolom Status Tab In Use

1. Client menandai tag Damaged/Missing di Global Settings hingga tersimpan (sesi API aktor)
2. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
3. Muat ulang Tab In Use setiap 5 detik sampai event diproses (batas tunggu 2 menit)
4. Verifikasi Status unit menjadi Damaged/Missing
5. Verifikasi unit tetap di Tab In Use

### TC-AC-ACTS-682: Event Condition pulih mengembalikan Status menjadi Available

6. Client memulihkan tag Damaged/Missing di Global Settings (Available atau Paired) hingga tersimpan (sesi API aktor)
7. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
8. Muat ulang Tab In Use setiap 5 detik sampai event diproses (batas tunggu 2 menit)
9. Verifikasi Status unit kembali Available
10. Client mengirim event status lain (Reserved, To be Returned, Retired) hingga tersimpan (sesi API aktor)
11. Tunggu 5 detik tanpa memuat ulang halaman
12. Verifikasi status unit tetap Available (tidak berubah oleh event status lain)

### TC-AC-ACTS-683: Combine tidak mengubah status unit dan menampilkan ikon

13. Combine unit RFID dan NFC Available di TAG > Combine & Separate hingga tersimpan (fixture BE)
14. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
15. Verifikasi ikon 🔗 muncul pada unit
16. Verifikasi Status tetap Available

### TC-AC-ACTS-684: Separate menghapus ikon tanpa mengubah status unit

17. Separate set Combined di TAG > Combine & Separate hingga tersimpan (fixture BE)
18. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
19. Verifikasi ikon 🔗 hilang
20. Verifikasi Status tetap Available

### TC-AC-ACTS-781: Event Condition atau Delete TAG atas unit non-In Use, terhapus, atau tak dikenal adalah no-op sukses

21. Catat Last Updated SKU, jumlah entri Activity Log, jumlah unit SKU, serta Status dan Condition U1 dan U2
22. Client mengirim event Condition Damaged/Missing untuk U1, U2, U3, dan TAG Code tak dikenal hingga tersimpan (sesi API aktor)
23. Client mengirim event Delete TAG untuk U1 lalu mengirim ulang event yang sama hingga tersimpan (sesi API aktor)
24. Tunggu 5 detik tanpa memuat ulang halaman
25. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available dan Tab In Use
26. Verifikasi semua event di-ack tanpa retry atau dead-letter
27. Verifikasi Status dan Condition U1 dan U2 tidak berubah terhadap baseline
28. Verifikasi tidak ada unit dibuat atau dihapus (jumlah unit SKU sama dengan baseline)
29. Buka Activity Log
30. Verifikasi tidak ada entri baru di Activity Log (jumlah entri sama dengan baseline)
31. Verifikasi Last Updated SKU tidak berubah terhadap baseline

### TC-AC-ACTS-782: Status kembali kosong setelah Delete TAG Jalur A dan kosong sampai event Condition pertama setelah aktivasi berikutnya

32. Client menghapus tag unit di Global Settings hingga tersimpan (sesi API aktor)
33. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
34. Muat ulang Tab Available setiap 5 detik sampai event diproses (batas tunggu 2 menit)
35. Verifikasi unit kembali Available di Tab Available
36. Client mengaktivasi ulang unit yang sama hingga tersimpan (sesi API aktor)
37. Buka Tab In Use sebelum event Condition baru
38. Verifikasi kolom Status unit menampilkan `—` (bukan Available maupun Damaged/Missing lama)
39. Client mengirim event Condition Damaged/Missing hingga tersimpan (sesi API aktor)
40. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
41. Muat ulang Tab In Use
42. Verifikasi Status unit menjadi Damaged/Missing

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (42 langkah); alasan: semua blok satu kelas harness (event lintas modul dari Global Settings) dan satu dataset unit, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pemicu Client lewat sesi API aktor bukan konteks kedua (P-2 tidak dipakai; keputusan 2026-10-30). Pelaku ditulis "hingga tersimpan" (R-20).
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline (S-12), membuka layar baca, dan memuat ulang tiap 5 detik memakai idiom baku "polling worker commit" (bagian 6, batas tunggu 2 menit).
- Absence entri Activity Log dan unit pada TC-AC-ACTS-781 memakai baseline (asersi jumlah, bukan kelas g) dan didahului anchor positif (tab dan tabel yang sama tampil; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-683 dan TC-AC-ACTS-684 menyebut Combine dan Separate di TAG > Combine & Separate tanpa langkah UI; spec menuliskannya sebagai pemicu fixture BE.
  - TC-AC-ACTS-682 menyebut "status lain tidak mengubah apa pun" tanpa cara memicunya; spec memicu event status lewat sesi API aktor.
  - TC-AC-ACTS-781 menyebut "di-ack tanpa retry atau dead-letter" tanpa cara mengamati; disediakan tim FE/BE.
