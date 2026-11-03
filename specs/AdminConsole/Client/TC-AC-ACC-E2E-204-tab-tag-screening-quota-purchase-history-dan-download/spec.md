---
id: TC-AC-ACC-E2E-204-tab-tag-screening-quota-purchase-history-dan-download
title: "Tab TAG: Screening Quota dan Purchase History, Filter Panel, Download, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-284
  - TC-AC-ACC-288
  - TC-AC-ACC-287
  - TC-AC-ACC-471
  - TC-AC-ACC-289
coverage:
  web: automated
---

# Tab TAG: Screening Quota dan Purchase History, Filter Panel, Download, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi" (Quota TAG terisi; TAG P-T1 (Type RFID / Qty 100 / CV Mitra Sejati / Andi Wijaya / 10 Feb 2026 09:00), P-T2 (NFC / 50 / PT Distribusi Nusantara / Budi Santoso / 12 Apr 2026 10:00), P-T3 (RFID / 25 / CV Mitra Sejati / Citra Dewi / 30 Jun 2026 13:00)), C-09 "PT Baru Daftar" (tanpa kuota/riwayat). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.
- Kemampuan teknis: pembacaan berkas unduhan (nama berkas CSV dan XLSX) oleh browser; tidak memeriksa isi berkas.

## Test Steps

### TC-AC-ACC-284: Screening Tab TAG

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `TAG`
4. Verifikasi tab aktif `TAG`
5. Verifikasi Section Quota memiliki toolbar `Download`
6. Verifikasi tabel Quota berkolom `Type | Total Quota | Used | Available` dengan baris QR selalu ada (QR/RFID/NFC/BLE/GPS)
7. Verifikasi Section Purchase History TAG memiliki toolbar Search dengan placeholder "Search by type, source, or action by...", `Filter`, dan `Download`
8. Verifikasi tabel Purchase History TAG berkolom `Type | Qty | Source | Action by | Date | ⋯`
9. Verifikasi Pagination Purchase History TAG default 10

### TC-AC-ACC-288: Client tidak memiliki Allocation History Out

10. Periksa Tab `TAG`
11. Verifikasi Tab `TAG` hanya memuat Section Quota dan Section Purchase History TAG; tidak ada riwayat alokasi keluar

### TC-AC-ACC-287: Screening Filter Purchase History TAG: label, placeholder, dan urutan awal Date Newest First

12. Lihat urutan awal baris Purchase History TAG
13. Verifikasi urutan awal (Newest First): P-T3 (Qty 25), P-T2 (Qty 50), P-T1 (Qty 100)
14. Klik Filter pada toolbar Purchase History TAG
15. Verifikasi Type: dropdown multi-select searchable, placeholder "All types"
16. Verifikasi Qty: field range dengan placeholder "Min" dan "Max"
17. Verifikasi Source: dropdown multi-select searchable, placeholder "All sources"
18. Verifikasi Date: date range picker satu field, placeholder "Select date"
19. Verifikasi Action by: dropdown multi-select searchable, placeholder "All users"
20. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
21. Klik ulang icon Filter untuk menutup panel Filter

### TC-AC-ACC-471: Download Quota TAG dan Purchase History TAG: toolbar Download dan nama file

22. Lihat toolbar Section Quota
23. Verifikasi Section Quota memiliki toolbar `Download` tanpa Search dan tanpa Filter
24. Klik Download Quota lalu pilih CSV
25. Klik Download Purchase History lalu pilih XLSX
26. Verifikasi tidak ada toast sukses
27. Verifikasi berkas `Client-TAG-PT Sejahtera Abadi` terunduh
28. Verifikasi berkas `Purchase-TAG-PT Sejahtera Abadi` terunduh

### TC-AC-ACC-289: Tab TAG tanpa kuota: Quota menampilkan nol (tanpa empty state) dan Purchase History empty state

29. Kembali ke List lewat breadcrumb Client
30. Ganti isi Search dengan `PT Baru Daftar`, tekan Enter
31. Klik Company Name "PT Baru Daftar" untuk membuka Detail
32. Klik Tab `TAG`
33. Verifikasi baris QR tetap tampil dengan Total Quota 0, Used 0, Available 0
34. Verifikasi empty state kuota tidak tampil
35. Verifikasi Purchase History menampilkan "No purchase history yet" dan "TAG quota purchase history will appear here."

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah klik ulang icon Filter untuk menutup panel (D-001) adalah langkah penghubung (S-03). TC-471 diletakkan sesudah screening; TC-289 memakai Client berbeda sehingga di akhir.
- Temuan untuk QA (S-15): TC-284 menyebut Quota baris QR/RFID/NFC/BLE/GPS tanpa nilai pada C-01 (Tabel A2 hanya "terisi"); nilai tidak diasersi. Post Condition seluruh TC `-` sehingga tidak diasersi.
