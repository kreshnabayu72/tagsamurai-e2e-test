---
id: TC-GS-TAG-E2E-013-capability-dicabut-saat-sesi-activate-terbuka
title: "Capability Manage TAG Dicabut Saat Sesi Activate Terbuka: Commit Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-320
coverage:
  web: automated
---

# Capability Manage TAG Dicabut Saat Sesi Activate Terbuka: Commit Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Manage TAG (Update) Client A (Agus Wijaya) `manageTagUpdate_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TAG_UPDATE_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; dicatat di `suite.md` bagian Kredensial). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Pelaku kedua (Admin B): Total Control kedua Client A (Dewi Lestari) `totalControl2_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC2_PASSWORD`, memakai sesi API sebagai pemicu saja (P-2); kesamaan akun dengan env var `GS_TC2` dikonfirmasi tim FE (Q-2). Mekanisme API pencabutan capability disediakan tim FE (tidak didefinisikan di TC, PRD, atau LLD).
- Data: stok resmi Admin Console Client A DD-S1 (GPS `356938035643001`, Available); kuota GPS tersedia. Stok di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE).
- State global: capability `Manage TAG` akun Manage TAG (Update) dicabut pada langkah 3 dan dipulihkan ke Manage TAG (Update) pada langkah 6 serta hook `after` sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: sesi API admin kedua untuk mencabut dan memulihkan capability; kemampuan baca status identifier lewat fixture BE (untuk Expected "tag tidak teraktivasi").
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach`.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Selektor: radio overlay Select TAG Type dan input entri manual GPS belum punya ID/aria-label di sumber; diselesaikan tim FE di tahap script.

## Test Steps

### TC-GS-TAG-320: Capability dicabut saat sesi Activate terbuka: commit ditolak server

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
2. Ketik `356938035643001` di input entri manual, klik `Add`
3. Cabut capability `Manage TAG` akun Manage TAG (Update) lewat sesi API Admin B hingga tersimpan
4. Klik `Submit`
5. Klik `Submit` pada dialog `Submit Activation`
6. Verifikasi toast error `You don't have permission to do this.`
7. Verifikasi tag `356938035643001` tidak teraktivasi (status identifier dibaca lewat fixture BE)
8. Pulihkan capability `Manage TAG` (Update) akun lewat sesi API Admin B hingga tersimpan
9. Klik item sidebar `TAG`, lalu klik `[Leave]` pada dialog `Unsaved Changes`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 7d). TC-320 berlabel `Manual Only — (d) dua sesi paralel` di TC; tetap masuk spec (D-4).
- Pengecualian P-2: sesi Admin B hanya memicu perubahan state (pencabutan capability) lewat sesi API dan bukan objek asersi; langkah 3 dan 8 ditulis "hingga ... tersimpan".
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 (membuka halaman Activate), langkah 8 (pemulihan capability; hook `after` sebagai cadangan, S-09), langkah 9 (kembali ke List dari halaman Activate yang masih berisi staging lewat sidebar `TAG` lalu `[Leave]`; `[Leave]` pada dialog `Unsaved Changes` tidak diasersi terpisah).
- Temuan untuk QA:
  - TC-320 langkah 2 menyebut "sesi Total Control" tanpa menyebut akun; Pre-setup Total Control kedua (`totalControl2_automated_qaTeam1`) berbeda nama dengan env `GS_TC2` (`totalControlSecond_automated_qaTeam1`) (Q-2).
  - TC-320 Expected tidak menyebut keadaan UI setelah penolakan (halaman Activate tetap atau tidak); spec hanya mengasersi toast dan state data.
  - TC-320 tidak menyebut cara teramati "tag tidak teraktivasi"; spec memakai kemampuan baca status lewat fixture BE (tanpa endpoint karangan, S-13).
  - Post Condition bernilai `-`.
