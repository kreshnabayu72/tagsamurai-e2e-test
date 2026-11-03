---
id: TC-FA-FAAM-E2E-109-popup-detail-progres-kepatuhan-tag-type-tidak-tampil-dua-tipe-dan-non-tag
title: "Popup Detail: Progres Kepatuhan TAG Type Tidak Tampil, Dua Tipe Wajib, dan Asset Name Non-TAG"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-833
  - TC-FA-FAAM-835
  - TC-FA-FAAM-836
coverage:
  web: automated
---

# Popup Detail: Progres Kepatuhan TAG Type Tidak Tampil, Dua Tipe Wajib, dan Asset Name Non-TAG

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`). Spec ini tidak memakai seed API per TC.
- Data Pre-setup yang hanya dibaca (tidak ada data yang diubah):
  - Pre-setup #13: `Warehouse Pallet` (Non-TAG, Total Asset 0), fixture `Fixture.faAssetName.warehousePallet`.
  - Pre-setup #38c: `Draft Only Item` (Total Asset 2, kedua aset berlifecycle `Draft`, tanpa aset `Active`).
  - Pre-setup #38d: `Multi Type Item` (TAG Type `RFID` dan `NFC`), 4 aset `Active`: aset 1 ber-Tag `Paired` RFID dan NFC; aset 2 hanya RFID; aset 3 `Not Paired Yet`; aset 4 ber-Tag `Paired` RFID, NFC, dan QR (QR Non-standard). Aset sesuai: hanya aset 1 (`[Compliant]` 1, `[N]` 4).
  - Pre-setup #38e: `Non-TAG Stock Item` (TAG Type `Non-TAG`), 3 aset `Active`: 2 aset tanpa Tag dan 1 aset ber-Tag `Paired` QR (Non-standard menurut `FATAG-LOGIC-03d`). `[Compliant]` 2, `[N]` 3.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-833: Baris progres tidak tampil bila Asset Name tanpa aset atau tanpa aset Active

1. Ketik Search `Warehouse Pallet`, tekan Enter
2. Klik nama `Warehouse Pallet`
3. Verifikasi TAG Type menampilkan teks `Non-TAG`
4. Verifikasi tidak ada baris progres kepatuhan di bawah nilai TAG Type `Non-TAG`
5. Verifikasi Identitas Utama lain tampil normal tanpa ruang kosong tersisa
6. Verifikasi tidak ada teks `0 / 0` atau teks progres sementara
7. Klik icon `[✕]` untuk menutup popup
8. Ganti isi kotak search dengan `Draft Only Item`, tekan Enter
9. Klik nama `Draft Only Item`
10. Verifikasi Identitas Utama tampil
11. Verifikasi label tab `Total Assets (2)` tampil
12. Verifikasi tidak ada baris progres kepatuhan pada Identitas Utama
13. Verifikasi tidak ada teks `0 / 0` atau teks progres sementara
14. Klik icon `[✕]` untuk menutup popup

### TC-FA-FAAM-835: Asset Name dengan dua tipe wajib

15. Ganti isi kotak search dengan `Multi Type Item`, tekan Enter
16. Klik nama `Multi Type Item`
17. Verifikasi baris progres `1 / 4 assets match the TAG type`
18. Verifikasi hanya aset 1 yang terhitung, sedangkan aset 2 (kurang satu tipe wajib), aset 3 (`Not Paired Yet`), dan aset 4 (Non-standard) tidak terhitung
19. Klik icon `[✕]` untuk menutup popup

### TC-FA-FAAM-836: Asset Name Non-TAG ber-aset, aset ber-Tag Paired terhitung Non-standard

20. Ganti isi kotak search dengan `Non-TAG Stock Item`, tekan Enter
21. Klik nama `Non-TAG Stock Item`
22. Verifikasi baris progres `2 / 3 assets match the TAG type`
23. Verifikasi aset ber-Tag `Paired` QR tidak terhitung dan dua aset tanpa Tag terhitung
24. Klik icon `[✕]` untuk menutup popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1, 8, 15, 20) dan `[✕]` menutup popup (langkah 7, 14, 19, 24).
- Asersi absence pada langkah 4 memakai nilai TAG Type `Non-TAG` pada langkah 3 sebagai anchor, dan pada langkah 12 memakai Identitas Utama dan label tab pada langkah 10 dan 11 sebagai anchor.
- Langkah 18 dan 23 adalah kesimpulan penghitungan yang tidak teramati terpisah dari teks pada langkah 17 dan 22; keduanya ditulis sebagai `Verifikasi` sendiri karena Expected TC memuatnya sebagai butir b.
- Temuan untuk QA:
  - TC-FA-FAAM-833 Expected a ("tanpa ruang kosong tersisa") adalah klaim tata letak tanpa ukuran; spec mengasersi bahwa Identitas Utama lain tampil lengkap.
  - TC-FA-FAAM-835 dan TC-FA-FAAM-836 Expected b tidak punya cara observasi per aset di UI selain pembilang dan penyebut baris progres; spec mengamati kesimpulannya dari pembilang.
