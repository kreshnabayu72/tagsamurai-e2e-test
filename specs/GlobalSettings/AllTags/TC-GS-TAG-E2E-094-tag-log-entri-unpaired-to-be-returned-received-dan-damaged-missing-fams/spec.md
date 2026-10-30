---
id: TC-GS-TAG-E2E-094-tag-log-entri-unpaired-to-be-returned-received-dan-damaged-missing-fams
title: "TAG Log: Entri Unpaired per Reason, To be Returned dan Received, serta Marked Damaged/Missing dari Receive Manually"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-281
  - TC-GS-TAG-282
  - TC-GS-TAG-364
  - TC-GS-TAG-365
coverage:
  web: automated
---

# TAG Log: Entri Unpaired per Reason, To be Returned dan Received, serta Marked Damaged/Missing dari Receive Manually

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client Log Wulan Sari `totalControl_automated_qaLog@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_LOG_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai). Login sekali di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data Pre-setup Client Log (dibaca saja, tanpa aksi tulis; fixture TAG Log DD-46 sampai DD-58, Tabel Data Uji Dinamis TC, dibuat lewat fixture BE; mekanisme dan pelaku fixture disediakan tim FE/BE, lihat Temuan untuk QA):

| ID | Code | Riwayat yang diasersi |
|---|---|---|
| DD-46 | `E2801160600002054D8C0046` | `Activated`; `Paired`; `Unpaired` Reason `Manual unpair`, Status `Paired` → `Available` |
| DD-47 | `E2801160600002054D8C0047` | `Activated`; `Paired`; `Unpaired` Reason `Replaced by E2801160600002054D8C0057`, Status `Paired` → `Damaged/Missing` (tag lama tidak dipindai; satu entri) |
| DD-48 | `E2801160600002054D8C0048` | `Activated`; `Paired`; `Unpaired` Reason `Changed TAG Type`, Status `Paired` → `Available` |
| DD-54 | `E2801160600002054D8C0054` | `Activated`; `Paired` ke Asset; `To be Returned` (Asset, Asset Code, Reason `Disposal`, Return Group `Gudang Pusat`) oleh pelaku disposal (user FAMS) |
| DD-57 | `E2801160600002054D8C0057` | `Activated`; `Paired` ke Asset; `Unpaired` Reason `Removed (no replacement)`, Status `Paired` → `Available` (tag Non-standard dilepas tanpa tag pengganti pada Replace TAG di FAMS; tag lama dipindai) |
| DD-58 | `E2801160600002054D8C0058` | `Activated`; `Paired` ke Asset; `To be Returned` (Return Group `Gudang Pusat`); `Marked Damaged/Missing` oleh Rina Wulandari (penerima, FAMS `Receive Manually`), Previous Status `To be Returned`, Note `Tag patah saat diterima` |

- Pelaku fixture (pelaku Unpaired DD-46 sampai DD-48, DD-57, pelaku disposal DD-54, Asset dan Asset Code DD-54) tidak disebut TC dan dibaca dari fixture (Q-15). Pelaku tampil sebagai `[First Name] [Last Initial]`: `Rina W` (Rina Wulandari).
- Kemampuan teknis: mengatur fixture TAG Log di atas pada Client Log; Search registri agar baris target tampil.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-TAG-281: Entri Unpaired per Reason, baris Status sebelum ke sesudah

1. Ketik Search `E2801160600002054D8C0046`, tekan Enter, buka menu baris DD-46, klik `TAG Log`
2. Verifikasi entri `TAG Unpaired by` pelaku memuat `Type` beserta baris turunannya, `Reason: Manual unpair` (bukan `Returned` maupun `Disposal`), dan `Status: Paired → Available`
3. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `E2801160600002054D8C0047`, tekan Enter, buka menu baris DD-47, klik `TAG Log`
4. Verifikasi entri `TAG Unpaired by` pelaku memuat `Type` beserta baris turunannya, `Reason: Replaced by E2801160600002054D8C0057` (bukan `Returned` maupun `Disposal`), dan `Status: Paired → Damaged/Missing`
5. Verifikasi TAG Log DD-47 memuat tepat satu entri `TAG Unpaired by`
6. Verifikasi tidak ada entri `TAG Marked Damaged/Missing by ...` maupun `TAG Retired by ...` terpisah pada TAG Log DD-47
7. Tutup popup lewat `[✕]`, ganti isi kotak search dengan `E2801160600002054D8C0048`, tekan Enter, buka menu baris DD-48, klik `TAG Log`
8. Verifikasi entri `TAG Unpaired by` pelaku memuat `Type` beserta baris turunannya, `Reason: Changed TAG Type` (bukan `Returned` maupun `Disposal`), dan `Status: Paired → Available`
9. Tutup popup lewat `[✕]`

### TC-GS-TAG-282: Entri To be Returned dari disposal, Reason Disposal dan Return Group, tanpa entri Unpaired maupun Retired

10. Ganti isi kotak search dengan `E2801160600002054D8C0054`, tekan Enter, buka menu baris DD-54, klik `TAG Log`
11. Verifikasi entri `TAG Marked To be Returned by` pelaku disposal memuat `Asset`, `Asset Code`, `Reason: Disposal`, dan `Return Group: Gudang Pusat`
12. Verifikasi `Return Group` `Gudang Pusat` sama dengan Disposal Group transaksi disposal pada fixture
13. Verifikasi tidak ada entri `TAG Unpaired by ...` maupun `TAG Retired by ...` dari disposal itu pada TAG Log DD-54
14. Tutup popup lewat `[✕]`

### TC-GS-TAG-364: Entri Unpaired Reason Removed (no replacement) untuk Replace TAG tanpa tag pengganti

15. Ganti isi kotak search dengan `E2801160600002054D8C0057`, tekan Enter, buka menu baris DD-57, klik `TAG Log`
16. Verifikasi TAG Log DD-57 memuat satu entri `TAG Unpaired by` pelaku user FAMS dengan `Reason: Removed (no replacement)`
17. Verifikasi entri Unpaired DD-57 memuat baris `Status: Paired → Available`
18. Verifikasi tidak ada entri `Marked Damaged/Missing` atau `Retired` terpisah pada TAG Log DD-57
19. Verifikasi tidak ada Reason `Replaced by ...` pada TAG Log DD-57
20. Tutup popup lewat `[✕]`

### TC-GS-TAG-365: Entri Marked Damaged/Missing dari Receive Manually memuat Note dan pelaku penerima

21. Ganti isi kotak search dengan `E2801160600002054D8C0058`, tekan Enter, buka menu baris DD-58, klik `TAG Log`
22. Verifikasi entri `TAG Marked Damaged/Missing by Rina W` (pelaku = penerima di FAMS)
23. Verifikasi entri `TAG Marked Damaged/Missing by Rina W` memuat baris `Previous Status: To be Returned`
24. Verifikasi entri `TAG Marked Damaged/Missing by Rina W` memuat baris `Note: Tag patah saat diterima`
25. Verifikasi entri `To be Returned` sebelumnya memuat `Return Group: Gudang Pusat`
26. Verifikasi penerimaan DD-58 tidak menulis entri `TAG Unpaired by ...` pada TAG Log DD-58
27. Tutup popup lewat `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec hanya membaca data.
- Urutan TC dalam spec sama dengan sumber (281, 282, 364, 365). Pengelompokan dataset (Client Log, fixture TAG Log) sama untuk keempat TC.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1, 3, 7, 10, 15, 21 (Search agar baris target tampil dan membuka TAG Log), langkah 3, 7, 9, 14, 20, 27 (menutup popup).
- Klausa Expected b TC-281 (Reason bukan `Returned` maupun `Disposal`) ditulis pada tiap `Verifikasi` Reason entri Unpaired DD-46, DD-47, dan DD-48 (langkah 2, 4, 8). Langkah 26 (penerimaan tidak menulis entri `Unpaired`) menjalankan klausa yang sama untuk DD-58 dan langkah 13 (disposal tidak menulis entri `Unpaired`) untuk DD-54. TC-281 langkah 1 hanya membuka DD-46 sampai DD-48, sehingga langkah 26 adalah asersi tambahan yang dicatat sesuai S-03: penerimaan pengembalian memakai DD-58 karena TC-281 tidak menyebut tag penerimaan.
- Langkah 5, 6, 13, 18, 19, 26 (absence) memakai entri lain pada popup yang sama sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-281 Expected b ("penerimaan pengembalian dan disposal tidak menulis entri `Unpaired`") tidak punya langkah observasi pada TC-281; spec mengamatinya pada DD-54 (disposal) dan DD-58 (penerimaan) dan mencatatnya sebagai asersi tambahan.
  - TC-282 Expected b ("`Return Group` berupa Disposal Group transaksi disposal") tidak dapat diamati terpisah dari Expected a di registri Global Settings; spec membandingkan dengan Disposal Group pada fixture transaksi disposal (disediakan tim FE/BE).
  - Pelaku fixture dan nama aset DD-54 tidak ditetapkan di Tabel Data Uji Dinamis (placeholder `[pelaku ...]`); spec mengasersi judul tanpa nama pelaku bila nilainya tidak ditetapkan (Q-15).
  - TC-364 Expected a menulis pelaku `[pelaku user FAMS]` tanpa nama; TC-365 menulis `[Rina Wulandari]` di Expected sedangkan format tampil pelaku adalah `[First Name] [Last Initial]` (`Rina W`); spec memakai `Rina W`.
  - Pembuatan fixture TAG Log (DD-46 sampai DD-58) antar spec tidak didefinisikan di TC (Q-4).
