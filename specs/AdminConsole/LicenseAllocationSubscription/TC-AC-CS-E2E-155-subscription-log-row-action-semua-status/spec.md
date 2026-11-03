---
id: TC-AC-CS-E2E-155-subscription-log-row-action-semua-status
title: "Subscription Log: Row Action pada Semua Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-590
coverage:
  web: automated
---

# Subscription Log: Row Action pada Semua Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data Pre-setup (baca-saja; spec tidak menulis data):

| Tab | Subscription ID | Status | Pre-setup |
|---|---|---|---|
| Current | `SUBS-20260101-00001` | Active | #61 |
| Current | `SUBS-20260819-00001` | Waiting for Approval | #49 |
| Current | `SUBS-20260819-00002` | Pending | #57 |
| Current | `SUBS-20250819-00002` | Expired | #50 |
| Current | `SUBS-20260810-00001` | Trial Active | #60 |
| History | `SUBS-20250101-00001` | Renewed | #62 |
| History | `SUBS-20260812-00001` | Rejected | #52 |
| History | `SUBS-20260805-00001` | Canceled | #56 |
| History | `SUBS-20260101-00002` | Archive | #58 |
| History | `SUBS-20260501-00001` | Trial Converted | #66 |

- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-590: Row action Subscription Log tampil di kedua tab pada semua status

1. Untuk setiap baris tab `Current` pada tabel Prerequisites (langkah 2 sampai 6): ulangi langkah 2 sampai 6
2. Ganti isi kotak search dengan `<Subscription ID baris>`, tekan Enter
3. Klik ikon `⋯` pada baris
4. Verifikasi item `Subscription Log` ada pada menu row action tepat setelah item Detail
5. Verifikasi item `Subscription Log` memakai ikon `FileHistoryLine` dengan severity dark
6. Tutup menu row action dengan tekan `Esc`
7. Klik tab `History`
8. Untuk setiap baris tab `History` pada tabel Prerequisites (langkah 2 sampai 6): ulangi langkah 2 sampai 6
9. Ganti isi kotak search dengan `SUBS-20260812-00001`, tekan Enter
10. Klik ikon `⋯` pada baris `SUBS-20260812-00001`, klik `Subscription Log`
11. Verifikasi modal Subscription Log terbuka dengan Subscription ID `SUBS-20260812-00001`
12. Verifikasi `Status:` badge Rejected pada header modal
13. Klik `[✕]`
14. Klik baris `SUBS-20260812-00001`
15. Verifikasi Subscription Detail `SUBS-20260812-00001` terbuka dan modal Subscription Log tidak tampil

## Notes

- Langkah berulang (bagian 8b butir 7): langkah 2 sampai 6 diulang untuk 5 baris tab `Current` (langkah 1) dan 5 baris tab `History` (langkah 8); ekspansi sekitar 58 langkah. Alasan di atas ~35 langkah: satu topik dan satu dataset, parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa (S-01).
- Langkah penghubung (S-03): langkah 2 dan 9 (Search untuk menemukan baris target pada dataset berhalaman 10 baris, R-16), langkah 6 (menutup menu row action), langkah 7 (pindah tab), dan langkah 13 (menutup modal).
- Subjudul `###` memetakan langkah ke id TC granular.
- Temuan untuk QA:
  - TC-AC-CS-590 Expected a ("Item Subscription Log ada pada semua baris di kedua tab") hanya menyebut 10 baris contoh; baris lain pada tab tidak diperiksa.
