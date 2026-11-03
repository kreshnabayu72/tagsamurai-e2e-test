---
id: TC-AC-ACC-E2E-189-badge-produk-dan-kuota-term-trial
title: "Term Trial: Badge Produk di List, Subscription Details Hasil Convert, dan Kuota Terpisah dari Term Paid"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-1022
  - TC-AC-ACC-1024
coverage:
  web: automated
---

# Term Trial: Badge Produk di List, Subscription Details Hasil Convert, dan Kuota Terpisah dari Term Paid

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-FX17-5 "PT Trial Aktif Saja" (Active; SAMS Trial Active satu-satunya term; FAMS dan SIEM tanpa subscription), C-FX17-6 "PT Trial Sudah Convert" (Active; SAMS Trial Converted dan term paid hasil Convert Active), C-FX18-1 "PT Kuota Trial Terpisah" (Active; FAMS Trial Active satu-satunya term FAMS dengan baris Asset Trial Total 50, Used 12; SAMS Active paid dengan asset license 80). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-1022: Badge produk menghitung baris Trial

1. Klik sub-tab `Active`, ketik Search `PT Trial Aktif Saja`, tekan Enter
2. Verifikasi sel SAMS baris "PT Trial Aktif Saja" menampilkan badge `Active`
3. Verifikasi sel FAMS baris "PT Trial Aktif Saja" berisi teks "No Subscription" (teks sel, bukan badge)
4. Ganti isi Search dengan `PT Trial Sudah Convert`, tekan Enter
5. Verifikasi sel SAMS baris "PT Trial Sudah Convert" menampilkan badge `Active` (term paid hasil Convert)
6. Verifikasi label `Converted` tidak tampil pada sel SAMS baris "PT Trial Sudah Convert"
7. Klik Company Name "PT Trial Sudah Convert" untuk membuka Detail
8. Klik Tab `Subscription`, sub-tab `SAMS`, lalu lihat Section "Subscription Details"
9. Verifikasi Section "Subscription Details" menampilkan term paid hasil Convert dengan status `Active`

### TC-AC-ACC-1024: Kartu License Quota menampilkan kuota term Trial sebagai satu baris Asset; kuota Trial tidak dijumlahkan ke Asset term paid maupun Total Quota QR

10. Kembali ke List lewat breadcrumb Client
11. Klik sub-tab `Active`, ganti isi Search dengan `PT Kuota Trial Terpisah`, tekan Enter
12. Klik Company Name "PT Kuota Trial Terpisah" untuk membuka Detail
13. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat tabel License Quota
14. Verifikasi tabel License Quota (term yang tampil adalah term Trial) memuat satu baris `Asset` dengan Total 50, Used 12, Available 38
15. Klik sub-tab `SAMS`, lalu lihat tabel License Quota
16. Verifikasi tabel License Quota SAMS (term yang tampil adalah term paid) memuat baris Asset dengan Total 80
17. Verifikasi tabel License Quota SAMS tidak memuat baris Asset milik term Trial
18. Klik Tab `TAG`, lalu lihat baris QR pada tabel Quota
19. Verifikasi baris QR Total Quota 80 (bukan 130; kuota Trial 50 tidak ikut dijumlahkan)
20. Verifikasi Available = Total − Used pada baris QR

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Temuan untuk QA (S-15): Post Condition kedua TC `-` sehingga tidak diasersi. TC-1022 menyebut sel FAMS "No Subscription" sebagai teks sel, bukan badge, sehingga spec mengasersi teks tanpa memeriksa severity.
