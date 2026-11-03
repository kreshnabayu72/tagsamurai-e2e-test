---
id: TC-AC-ACTS-E2E-201-approvals-tab-history-search-kolom-bagian-2-search-visibilitas
title: "Approvals Tab History: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-625
  - TC-AC-ACTS-626
  - TC-AC-ACTS-627
  - TC-AC-ACTS-628
  - TC-AC-ACTS-629
coverage:
  web: automated
---

# Approvals Tab History: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Tabel "Kolom uji Search" (Search hanya menyaring saat Enter):

| TC | Kolom | Keyword huruf kecil | Keyword huruf besar | Keyword tidak ada | Nilai yang dicari |
|---|---|---|---|---|---|
| 625 | Requested By | abc | ABC | zzz-tidak-ada-req | Subject oleh `PT ABC Logistics (Client)` |
| 626 | Approver | andi | ANDI | zzz-tidak-ada-app | Subject yang diputuskan Andi |

- Data tambahan: salah satu Subject memiliki Requested At atau Resolved At `17 Jun 2026` (nilai yang tampil di tabel, TC-AC-ACTS-627).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`
2. Verifikasi tabel memuat sedikitnya satu baris data

### TC-AC-ACTS-625 dan 626: Search kelas entitas dan user

3. Untuk setiap baris tabel "Kolom uji Search" di Prerequisites, lakukan langkah 4 sampai 10
4. Ketik Search `<keyword huruf kecil pada iterasi>`, tekan Enter
5. Verifikasi tabel memuat baris yang cocok dengan `<nilai yang dicari pada iterasi>` pada kolom `<kolom pada iterasi>`
6. Ganti isi kotak search dengan `<keyword huruf besar pada iterasi>`, tekan Enter
7. Verifikasi tabel memuat baris yang cocok dengan `<nilai yang dicari pada iterasi>` pada kolom `<kolom pada iterasi>`
8. Ganti isi kotak search dengan `<keyword tidak ada pada iterasi>`, tekan Enter
9. Verifikasi empty state `No results found`
10. Klik `(←)` pada kotak Search

### TC-AC-ACTS-627: Search tidak mencari kolom Requested At dan Resolved At

11. Ketik Search `17 Jun 2026`, tekan Enter
12. Verifikasi empty state `No results found` (tabel tidak menemukan baris berdasarkan nilai kolom Requested At dan Resolved At)
13. Klik `(←)` pada kotak Search
14. Klik icon Filter
15. Verifikasi field `Requested At` dan `Resolved At` tersedia di Filter Panel (penyaringan kolom tersebut hanya lewat Filter Panel)
16. Klik icon Filter untuk menutup panel

### TC-AC-ACTS-628: Search terikat visibilitas kolom, kolom `Approval` di-hide

17. Klik header (⋯), hilangkan centang kolom `Approval`
18. Verifikasi kolom `Approval` tidak tampil
19. Ketik Search `rejected`, tekan Enter
20. Verifikasi keyword `rejected` tidak mencocokkan baris melalui kolom `Approval`
21. Verifikasi tabel memuat sedikitnya satu baris yang cocok dengan `rejected` lewat kolom selain `Approval`
22. Klik `(←)` pada kotak Search

### TC-AC-ACTS-629: Search terikat visibilitas kolom, kolom `Approval` di-unhide kembali

23. Klik header (⋯), centang kembali kolom `Approval`
24. Verifikasi kolom `Approval` tampil kembali
25. Ketik Search `rejected`, tekan Enter
26. Verifikasi keyword `rejected` kembali mencocokkan baris melalui kolom `Approval`
27. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah yang diulang per kolom: langkah 4 sampai 10 (iterasi dari tabel "Kolom uji Search" di Prerequisites, 2 iterasi); `Verifikasi` tetap satu per klausa (bagian 8b butir 7). Langkah penghubung (S-03): klik `(←)` pada kotak Search (reset tabel), menutup panel Filter. Pembanding "sedikitnya satu baris" pada langkah 2 mendahului asersi absence dan hasil Search.
- Temuan untuk QA: (1) TC-AC-ACTS-628 butir b "baris yang cocok lewat kolom lain tetap bisa dicari" tidak menyebut data yang cocok lewat kolom lain untuk keyword `rejected`; spec mengasersi bahwa hasil Search hanya memuat baris yang cocok lewat kolom selain `Approval`. (2) TC-AC-ACTS-627 langkah 4 memakai contoh tanggal `17 Jun 2026`; data harus memuat tanggal itu.
