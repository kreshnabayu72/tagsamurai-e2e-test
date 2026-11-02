---
id: TC-AC-ACTS-E2E-007-guided-tooltip-stock-list-empat-step-navigasi-flag-dan-keyboard
title: "Guided Tooltip Stock List: Empat Step, Navigasi Next/Back/Done/Skip, Flag Seen, Keluar Tanpa Selesai, dan Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-24
  - TC-AC-ACTS-25
  - TC-AC-ACTS-26
  - TC-AC-ACTS-27
  - TC-AC-ACTS-28
coverage:
  web: automated
---

# Guided Tooltip Stock List: Empat Step, Navigasi Next/Back/Done/Skip, Flag Seen, Keluar Tanpa Selesai, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1.
- State global: flag `guided_tooltip_seen_ac-tag-stock` diatur spec ini sesudah hook `before` suite (pengecualian atas penyetelan `seen` di `suite.md`); kemampuan membaca dan menyetel flag (belum diset atau `true`) disediakan tim FE/BE tanpa endpoint karangan. Hook `after` suite memulihkan nilai awal flag.
- Kemampuan teknis: mengatur ukuran viewport browser (disediakan tim FE); viewport dipulihkan di langkah penghubung.
- Spec read-only terhadap data stok: tidak ada data Dinamis.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-24: Guided Tooltip kunjungan pertama menampilkan 4 step

1. Setel flag Guided Tooltip menjadi belum diset (fixture BE)
2. Klik menu sidebar TAG > Stock
3. Verifikasi Walkthrough otomatis mulai dari Step 1
4. Verifikasi Step 1 Table `TAG Stock Overview`: `This table shows all physical TAG inventory across RFID, NFC, BLE, and GPS types grouped by SKU.`
5. Verifikasi `[Back]` tersembunyi di Step 1
6. Klik `[Next]`
7. Verifikasi Step 2 Toolbar `Search & Filter`: `Narrow the table down to a specific SKU or a subset of stock. Available search fields and filters depend on the columns shown.`
8. Klik `[Next]`
9. Verifikasi Step 3 Kolom TAG Type `TAG Classifications`: `Identifies the physical TAG category for this SKU. Registration method depends on this classification.`
10. Klik `[Next]`
11. Verifikasi Step 4 Kolom Actions `Stock Actions`: `Access row-level operations to register new physical TAG batches or open this SKU's detail page.`
12. Verifikasi `[Next]` menjadi `[Done]` di Step terakhir

### TC-AC-ACTS-25: Navigasi Next, Back, Done, dan Skip

13. Klik `[Back]`
14. Verifikasi Walkthrough kembali ke Step 3
15. Klik `[Next]` kembali ke Step 4
16. Klik `[Done]` di Step 4
17. Verifikasi Walkthrough tertutup
18. Verifikasi Flag seen telah diatur (`true`)
19. Klik tombol `[?]` di kanan breadcrumb
20. Verifikasi Walkthrough mulai ulang dari Step 1
21. Verifikasi Flag seen tetap `true` (tidak direset oleh replay)
22. Klik `[Skip]`
23. Verifikasi Walkthrough tertutup dan flag seen tetap `true`
24. Klik tombol `[?]`, lalu klik overlay gelap
25. Verifikasi Walkthrough tertutup

### TC-AC-ACTS-26: Kunjungan berikutnya tidak otomatis muncul

26. Klik menu sidebar TAG > Stock
27. Verifikasi Breadcrumb `TAG > Stock` tampil
28. Verifikasi Walkthrough tidak muncul otomatis

### TC-AC-ACTS-27: Keluar tanpa selesai tidak mengatur flag seen

29. Setel flag Guided Tooltip menjadi belum diset (fixture BE)
30. Klik menu sidebar TAG > Stock untuk memulai walkthrough
31. Ubah ukuran viewport saat walkthrough berjalan
32. Verifikasi Walkthrough tertutup tanpa mengatur flag (flag tetap belum diset)
33. Pulihkan viewport ke ukuran semula
34. Klik menu sidebar TAG > Stock untuk memulai walkthrough, lalu klik menu sidebar halaman lain (Approvals) saat walkthrough berjalan
35. Klik menu sidebar TAG > Stock untuk kembali
36. Verifikasi Walkthrough muncul otomatis lagi
37. Verifikasi Flag tetap belum diset

### TC-AC-ACTS-28: Aksesibilitas keyboard

38. Tekan Tab untuk fokus
39. Verifikasi Kotak tooltip mendapat fokus keyboard
40. Tekan `→`
41. Verifikasi Walkthrough pindah ke step berikutnya (`→` = Next)
42. Tekan `Enter`
43. Verifikasi Walkthrough pindah ke step berikutnya (`Enter` = Next)
44. Tekan `←`
45. Verifikasi Walkthrough kembali ke step sebelumnya (`←` = Back)
46. Tekan `Esc`
47. Verifikasi Walkthrough tertutup (`Esc` = Skip)

## Notes

- Sekitar 35 langkah (di atas smell, 47 langkah): lima TC Guided Tooltip berbagi satu objek uji (walkthrough halaman TAG > Stock) dan flag yang sama; pemisahan per TC menambah login dan penyetelan flag tanpa menambah makna.
- P-4: lima TC berbagi state global flag Guided Tooltip yang dibangun berurutan; hook suite menyetel flag `seen` sebelum spec dan spec menulis keadaan awal flag tiap bagian di langkah pertama TC-nya.
- Langkah penghubung (S-03): menyetel flag lewat fixture BE; klik menu sidebar TAG > Stock mereset list; memulihkan viewport; klik `[Next]` kembali ke Step 4 sesudah `[Back]` agar `[Done]` dapat diklik.
- Temuan untuk QA (S-15): TC-AC-ACTS-25 butir b menulis "[Done] dan [Skip] menutup walkthrough dan mengatur flag seen" tetapi `[Done]` dijalankan lebih dulu sehingga flag sudah `true` saat `[Skip]`; penyetelan flag oleh Skip tidak teruji terpisah. `[Skip]` atau overlay gelap ditulis "atau" pada TC; spec menjalankan keduanya. TC-AC-ACTS-27 langkah 3 ("Buka halaman lain") tidak menyebut halaman; spec memakai Approvals. TC-AC-ACTS-28 tidak menyebut step awal saat `→` ditekan; spec mengasersi perpindahan relatif.
