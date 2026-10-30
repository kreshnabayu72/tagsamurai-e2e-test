---
id: TC-GS-TAG-E2E-012-tenant-suspended-expired-aksi-tulis-ditolak
title: "State Tenant: Aktivasi dan Delete Ditolak Server saat Client Suspended atau Expired"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-319
coverage:
  web: automated
---

# State Tenant: Aktivasi dan Delete Ditolak Server saat Client Suspended atau Expired

## Prerequisites

- Mode: FE+BE.
- Spec kelas h (state tenant). Akun aktor: Total Control Client Susp (Hana Susanti) `totalControl_automated_qaSusp@qwertysystem.net`, password `Spectra.env.GS_TC_SUSP_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; dicatat di `suite.md` bagian Kredensial). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Data Pre-setup (hanya dibaca): Client Susp berstatus Suspended; registri memuat tag Available `356938035643001` (target Delete); stok resmi Client Susp memuat IMEI `356938035643003` Available (target Activate). Data di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE).
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): pelaku perubahan status Client Susp ke Suspended atau Expired dan pemulihannya (langkah 2 dan 22).
- Kemampuan teknis (disediakan tim FE): sesi API admin/Admin Console untuk mengubah status Client Susp ke Suspended atau Expired (langkah 2 dan 22) dan memulihkannya ke Suspended; akun pelaku perubahan status tidak ada di Pre-setup TC dan ditulis "disediakan tim FE" (S-13). Pemulihan status ke nilai awal (Suspended) dilakukan lewat langkah 22 dan hook `after` sebagai cadangan.
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach`.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` disetel true untuk akun Client Susp oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Selektor: radio overlay Select TAG Type dan input entri manual GPS belum punya ID/aria-label di sumber; diselesaikan tim FE di tahap script.
- State global: status Client Susp (Suspended, lalu Expired, dikembalikan ke Suspended). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-319: Entitas Suspended atau Expired: aksi tulis ditolak server dengan toast khusus

1. Untuk setiap status Client pada tabel "Status Client" (Suspended, lalu Expired), lakukan langkah 2 sampai 21a

| Status Client | Keterangan |
|---|---|
| Suspended | status awal Pre-setup Client Susp |
| Expired | status diubah lewat sesi API, dipulihkan ke Suspended pada langkah 22 |

2. Setel status Client Susp sesuai baris tabel lewat sesi API (disediakan tim FE) hingga tersimpan
3. Muat ulang halaman Global Settings > TAG Tab All
4. Klik `+ Activate TAG`
5. Pilih `GPS` pada overlay `Select TAG Type`
6. Klik `Continue` pada popup `Ready to Activate a TAG`
7. Ketik `356938035643003` di input entri manual, klik `Add`
8. Klik `Submit`
9. Klik `Submit` pada dialog `Submit Activation`
10. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
11. Verifikasi tidak ada redirect (halaman tetap Activate TAG)
12. Klik item sidebar `TAG`, lalu klik `[Leave]` pada dialog `Unsaved Changes`
13. Ketik Search `356938035643003`, tekan Enter
14. Verifikasi empty state `No results found`
15. Klik `(←)` pada kotak Search
16. Buka menu baris tag Available `356938035643001`, klik `Delete`
17. Klik `Delete` pada dialog `Delete TAG`
18. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
19. Verifikasi tidak ada redirect
20. Ketik Search `356938035643001`, tekan Enter
21. Verifikasi tag `356938035643001` tetap ada di registri
21a. Klik `(←)` pada kotak Search
22. Pulihkan status Client Susp ke Suspended lewat sesi API hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 7d). Subjudul `###` memetakan langkah ke id TC granular.
- Judul dan Expected TC-319 menyebut "Suspended atau Expired" sedangkan Precondition dan Data Uji hanya Client Susp (Suspended). Spec mengikuti judul dan Expected dengan perulangan dua status (langkah 1 sampai 21a).
- Langkah 2 sampai 21a diulang untuk dua status (Suspended, Expired); parameter hanya status Client di tabel. Ekspansi: 21 langkah x 2 = 42 langkah. Untuk Suspended, langkah 2 hanya memastikan status awal.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 2 dan 3 (pemicu perubahan status dan muat ulang), langkah 12 (keluar dari halaman Activate dengan staging berisi lewat sidebar `TAG` lalu `[Leave]`; `[Leave]` pada dialog `Unsaved Changes` tidak diasersi terpisah), langkah 13 dan 20 (Search untuk menemukan baris target), langkah 15 dan 21a (`(←)`; 21a mengosongkan Search di akhir tiap iterasi), pemulihan status pada langkah 22.
- Langkah 14 (`No results found`) adalah anchor positif untuk absence hasil Search (8b butir 2) dan membuktikan tag stok tidak teraktivasi; langkah 21 membuktikan Delete tidak mengubah data.
- Alasan spec melewati sekitar 35 langkah (23 nominal, 42 ekspansi): satu TC satu kelas (h) dengan dua status Client yang menjalankan blok identik; blok Expired tidak bermakna bila status tidak dipulihkan, tetapi keduanya satu topik (aksi tulis ditolak) dan berbagi satu dataset.
- Temuan untuk QA:
  - TC-319 judul dan Expected mencakup Expired tetapi Precondition dan Data Uji hanya Client Susp berstatus Suspended; pelaku perubahan status ke Expired tidak ada di Pre-setup TC.
  - TC-319 langkah 2 ("Hapus tag Available lewat menu baris") tidak menyebut tag yang dihapus; spec memakai `356938035643001` dari Precondition.
  - TC-319 tidak menyebut cara keluar dari halaman Activate setelah penolakan; spec memakai sidebar `TAG` lalu `[Leave]` (jalur keluar yang disebut TC-113 butir c).
  - Post Condition bernilai `-`.
