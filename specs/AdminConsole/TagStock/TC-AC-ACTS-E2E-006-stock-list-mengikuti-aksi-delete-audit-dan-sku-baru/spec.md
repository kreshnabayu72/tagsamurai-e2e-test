---
id: TC-AC-ACTS-E2E-006-stock-list-mengikuti-aksi-delete-audit-dan-sku-baru
title: "Stock List Mengikuti Aksi: Available Mengikuti Transisi Status, Mutasi saat Terfilter, Urutan Deterministik, dan Last Updated Setelah Delete Unit Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-4
  - TC-AC-ACTS-97
  - TC-AC-ACTS-99
  - TC-AC-ACTS-889
coverage:
  web: automated
---

# Stock List Mengikuti Aksi: Available Mengikuti Transisi Status, Mutasi saat Terfilter, Urutan Deterministik, dan Last Updated Setelah Delete Unit Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1.
- Data seed milik spec (SKU bersuffix `{runId}-006`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): SKU F (RFID; 5 Available, 3 Damaged/Missing, 4 In Use) untuk TC-AC-ACTS-889; SKU G1 dan SKU G2 masing-masing Total Registered `1` untuk TC-AC-ACTS-99, bersama 11 SKU pengisi masing-masing Total Registered `2`; seluruh 13 SKU ber-Brand `Tie-{runId}-006` sehingga Search brand itu membatasi tabel ke 13 baris (lebih dari 10, ada halaman 2) dan pada Sort Total Registered Ascending G1 dan G2 (nilai sama) berada di halaman 1; SKU H dengan satu unit Available untuk TC-AC-ACTS-4. Untuk filter TAG Type RFID dipakai SKU RFID Pre-setup #12.
- Asersi Last Updated (TC-AC-ACTS-4) membandingkan dengan waktu yang dicatat sesudah `[Delete]` dengan toleransi satu menit; jam server dan jam browser sinkron.
- Kemampuan teknis: Audit TAG (Submit), Activate TAG di Global Settings > TAG, dan pendaftaran SKU GPS baru di Settings > Device SKU dipicu lewat sesi API aktor Total Control (login API; tidak dihitung sebagai sesi web); cara pemicu lintas modul tidak didefinisikan TC (disediakan tim FE/BE).
- Pemulihan: hook `after` menghapus SKU seed (termasuk SKU GPS baru yang didaftarkan TC-AC-ACTS-97) dan unit milik spec.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-97: Mutasi saat Stock List terfilter

1. Klik icon Filter, pilih `RFID` pada field `TAG Type`, klik `[Apply]`
2. Verifikasi Stock List memuat sedikitnya satu baris SKU RFID
3. Daftarkan SKU GPS baru (bersuffix `{runId}-006`) lewat sesi API aktor di Settings > Device SKU hingga SKU tersimpan
4. Tunggu aksi selesai
5. Klik icon Filter, lalu `[Apply]` tanpa mengubah kriteria untuk memuat ulang daftar
6. Verifikasi Baris SKU GPS baru tidak muncul pada hasil terfilter RFID
7. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACTS-99: Urutan deterministik untuk baris bernilai sama

8. Ketik Search `Tie-{runId}-006`, tekan Enter
9. Klik header `Total Registered` sampai Ascending
10. Catat urutan baris SKU G1 dan SKU G2 pada halaman 1
11. Pindah ke halaman 2, lalu kembali ke halaman 1
12. Verifikasi Urutan baris SKU G1 dan SKU G2 sama pada setiap request
13. Verifikasi Tidak ada baris ganda atau terlewat antar halaman
14. Klik header `Total Registered` dua kali lagi sampai kembali netral

### TC-AC-ACTS-889: Available mengikuti transisi status unit

15. Ganti isi kotak search dengan nama SKU F, tekan Enter
16. Catat Total Registered, Available, In Use, dan Damaged/Missing baris SKU F
17. Submit Audit TAG yang menandai 1 unit Available SKU F sebagai Damaged/Missing lewat sesi API aktor hingga Audit tersimpan
18. Tunggu aksi selesai
19. Klik menu sidebar TAG > Stock, lalu ketik Search nama SKU F, tekan Enter
20. Verifikasi Available `4`, Damaged/Missing `4`, dan Total Registered tetap `12` pada baris SKU F
21. Re-scan unit itu di Audit TAG lewat sesi API aktor hingga unit pulih ke Available tersimpan
22. Tunggu aksi selesai
23. Klik menu sidebar TAG > Stock, lalu ketik Search nama SKU F, tekan Enter
24. Verifikasi Available `5`, Damaged/Missing `3`, dan Total Registered tetap `12`
25. Activate TAG 1 unit Available SKU F di Global Settings > TAG lewat sesi API aktor hingga TAG teraktivasi tersimpan
26. Tunggu aksi selesai
27. Klik menu sidebar TAG > Stock, lalu ketik Search nama SKU F, tekan Enter
28. Verifikasi Available `4`, In Use `5`, dan Total Registered tetap `12`

### TC-AC-ACTS-4: Last Updated SKU yang seluruh unitnya dihapus (aksi hapus di akhir spec)

29. Hapus 1 unit Available SKU F lewat Detail SKU > Tab Available > row action Delete > `[Delete]`
30. Tunggu aksi selesai
31. Klik breadcrumb `Stock`, lalu ganti isi kotak search dengan nama SKU F, tekan Enter
32. Verifikasi Available `3` dan Total Registered `11` pada baris SKU F
33. Ganti isi kotak search dengan nama SKU H, tekan Enter
34. Hapus satu-satunya unit SKU H lewat Detail SKU > Tab Available > row action Delete > `[Delete]`
35. Tunggu aksi selesai
36. Catat waktu sesudah `[Delete]` (jam server dan jam browser sinkron)
37. Klik breadcrumb `Stock`, ganti isi kotak search dengan nama SKU H, tekan Enter
38. Verifikasi Baris SKU H tetap tampil dengan Total Registered `0`
39. Verifikasi Last Updated SKU H sama dengan waktu yang dicatat pada langkah 36 (toleransi satu menit), bukan `—`

## Notes

- Spec ini melewati sekitar 35 langkah (37 langkah); alasan: semua blok satu permukaan (Stock List) dengan pemicu lewat sesi API aktor, tiap blok TC berdiri sendiri, dan blok yang menghapus data (TC-AC-ACTS-4) berada di akhir sehingga kegagalannya tidak menutupi blok lain.
- Urutan TC: TC-AC-ACTS-97 dan TC-AC-ACTS-99 lebih dulu; langkah hapus unit SKU F (bagian Expected TC-AC-ACTS-889 butir d) dan TC-AC-ACTS-4 ditaruh di akhir karena menghapus data (S-10). Hapus unit SKU F dan asersinya ditulis di bawah heading TC-AC-ACTS-4 agar aksi menghapus berada di akhir spec.
- Langkah penghubung (S-03): Search nama SKU seed (R-16); `[Clear Field]` dan `[Apply]` mengosongkan Filter sebelum TC berikutnya (S-09); klik menu sidebar TAG > Stock mereset list sebelum membaca ulang angka; dua klik header terakhir mengembalikan urutan netral.
- Temuan untuk QA (S-15): TC-AC-ACTS-889 dan TC-AC-ACTS-4 memicu Audit TAG, Activate TAG, dan Delete tanpa langkah konkret lintas modul; langkah ditulis sebagai pemicu lewat sesi API aktor (disediakan tim FE/BE) tanpa endpoint karangan. TC-AC-ACTS-99 tidak menyebut dua SKU bernilai sama berada di halaman mana; spec memakai Total Registered Ascending dengan lebih dari 10 baris. TC-AC-ACTS-97 tidak menyebut cara memuat ulang tampilan; spec memakai Apply Filter ulang.
- Langkah penghubung tambahan (S-03, 8b butir 8): "Tunggu aksi selesai" (langkah 30 dan 35) sesudah `[Delete]` yang hasilnya tidak diasersi dan sebelum pindah surface lewat breadcrumb `Stock`.
