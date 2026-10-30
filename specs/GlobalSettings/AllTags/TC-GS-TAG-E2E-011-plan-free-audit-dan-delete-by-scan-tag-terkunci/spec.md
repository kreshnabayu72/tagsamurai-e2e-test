---
id: TC-GS-TAG-E2E-011-plan-free-audit-dan-delete-by-scan-tag-terkunci
title: "Plan Free: Audit atas Tipe Terkunci Tanpa Baris dan Delete by Scan atas Tag Terkunci Ditolak"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-175
coverage:
  web: automated
---

# Plan Free: Audit atas Tipe Terkunci Tanpa Baris dan Delete by Scan atas Tag Terkunci Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client Free (Joko Widodo) `totalControl_automated_qaFree@qwertysystem.net`, password `Spectra.env.GS_TC_FREE_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; dicatat di `suite.md` bagian Kredensial). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Data Pre-setup (hanya dibaca): Client Free memuat tag RFID warisan DD-F2 `E2801160600002054D8A6001` (Available, terkunci) dan QR DD-F1. Data di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE, D-4, Q-1): simulasi pemindai RFID yang tersambung (scan nilai `E2801160600002054D8A6001`, kemudian `Stop` pada Floating Status Widget). Mekanisme dan endpoint tidak didefinisikan di TC, PRD, maupun LLD; tidak dikarang di spec.
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach`.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Selektor: overlay Select TAG Type, popup Audit, dan Floating Status Widget belum punya ID/aria-label di sumber; diselesaikan tim FE di tahap script.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-175: Free plan: Audit atas tipe terkunci tidak memuat baris dan Delete by Scan atas tag terkunci ditolak

1. Klik `Audit TAG`
2. Pilih `RFID` pada overlay `Select TAG Type`
3. Verifikasi popup Audit menampilkan empty state `No TAGs to audit`
4. Verifikasi tombol `Submit` pada popup Audit disabled
5. Tutup popup Audit
6. Klik `Delete by Scan`
7. Pilih teknologi `RFID` pada overlay
8. Pindai `E2801160600002054D8A6001` (DD-F2)
9. Verifikasi toast error `You don't have permission to do this.`
10. Verifikasi tidak ada dialog konfirmasi
11. Klik `Stop` pada Floating Status Widget
12. Ketik Search `E2801160600002054D8A6001`, tekan Enter
13. Verifikasi tag DD-F2 tetap ada di registri

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 3h). TC-175 berlabel `Manual Only — (b)` di TC; tetap masuk spec (D-4, Q-1). Dipisah dari spec plan tier (spec 010) karena butuh harness scan (kelas d).
- Rujukan lintas spec: perilaku plan Free pada tombol Activate dan tag terkunci ada di spec 010 (TC-315, TC-316).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 5 (menutup popup), langkah 11 (`Stop` pada Floating Status Widget; konvensi `Pindai X` di Catatan TC memakai `Stop` sebelum menyentuh kontrol halaman lain, page-lock sesi scan), langkah 12 (Search untuk menemukan baris target). Langkah 13 mengasersi "tag tetap ada" (Expected b); langkah 9 menjadi anchor respons server.
- Temuan untuk QA:
  - TC-175 Expected a menyebut empty state `No TAGs to audit` tanpa deskripsi; PRD S-06 memuat deskripsi `There are no TAGs of this type waiting to be audited.` Spec hanya mengasersi judul sebagaimana TC.
  - TC-175 langkah 2 "Tutup popup" tidak menyebut cara menutup (`✕` atau `Esc`); spec memakai penutupan tanpa asersi.
  - Post Condition bernilai `-`.
