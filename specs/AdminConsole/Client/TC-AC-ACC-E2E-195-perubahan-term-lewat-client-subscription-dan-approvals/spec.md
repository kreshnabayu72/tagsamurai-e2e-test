---
id: TC-AC-ACC-E2E-195-perubahan-term-lewat-client-subscription-dan-approvals
title: "Perubahan Term dari Client Subscription dan Approvals: Reject Renewal, Renewal Expired/Grace, dan Cancel Term Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-269
  - TC-AC-ACC-270
  - TC-AC-ACC-662
  - TC-AC-ACC-271
coverage:
  web: automated
---

# Perubahan Term dari Client Subscription dan Approvals: Reject Renewal, Renewal Expired/Grace, dan Cancel Term Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dikonsumsi pada TC, ditiru bersuffix; di-seed hook `before` lewat Fixture BE yang disediakan tim FE/BE, Partner CV Mitra Sejati, Group Area Jakarta): (a) "PT Renewal Ditolak Uji {runId}-195" (atribut C-ISO-8: FAMS predecessor Active + Renewal Waiting for Approval, requester bukan GM/TC); (b) "PT Perpanjang Expired {runId}-195" (FAMS predecessor Expired yang memenuhi syarat Renewal; TC-270 tidak menyebut fixture, lihat Temuan untuk QA); (c) "PT Perpanjang Uji {runId}-195" (atribut C-LIF-7: FAMS Grace yang memenuhi syarat Renewal, Default User Activated); (d) "PT Batal Atas Arsip {runId}-195" (atribut C-W3LIF-2: Active, FAMS term lama Archive + term baru Active plan owner Principal, SAMS dan SIEM tidak pernah berlangganan, Default User Not Yet Activated). Hook `after` menghapus keempat Client lewat API.
- Alasan data bersuffix: seluruh TC mengonsumsi fixture (Reject, Renewal, Cancel, Auto-Archive) sehingga spec memakai Client sendiri (S-06, S-12).
- Kemampuan teknis: halaman Admin Console > Approvals (Reject Renewal), Admin Console > Client Subscription (Submit Renewal terotorisasi langsung dan Cancel Subscription), modal Changelog List. Suite berjalan serial (`parallel: false`).
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).

## Test Steps

### TC-AC-ACC-269: Renewal Waiting for Approval tidak menggantikan term live predecessor, termasuk setelah Reject

1. Ketik Search `PT Renewal Ditolak Uji {runId}-195`, tekan Enter
2. Verifikasi sel FAMS baris "PT Renewal Ditolak Uji {runId}-195" menampilkan badge `Active`
3. Klik Company Name "PT Renewal Ditolak Uji {runId}-195", lalu buka Tab `Subscription`, sub-tab `FAMS`
4. Verifikasi sub-tab `FAMS` menampilkan satu ringkasan term predecessor dengan Status badge `Active`
5. Verifikasi term Renewal Waiting for Approval tidak menggantikan ringkasan term predecessor
6. Reject Renewal "PT Renewal Ditolak Uji {runId}-195" dari Approvals
7. Tunggu aksi selesai, lalu buka Admin Console > Client, ketik Search `PT Renewal Ditolak Uji {runId}-195`, tekan Enter
8. Verifikasi sel FAMS tetap `Active` (predecessor)

### TC-AC-ACC-270: Renewal terotorisasi pada predecessor Expired: badge term baru Active

9. Submit Renewal terotorisasi langsung untuk FAMS "PT Perpanjang Expired {runId}-195" dari Admin Console > Client Subscription
10. Tunggu aksi selesai, lalu buka Admin Console > Client, ketik Search `PT Perpanjang Expired {runId}-195`, tekan Enter
11. Verifikasi sel FAMS baris "PT Perpanjang Expired {runId}-195" menampilkan badge term baru `Active`

### TC-AC-ACC-662: Subscription Details menampilkan satu term: setelah Renewal terotorisasi, term Grace digantikan term baru Active

12. Kembali ke List lewat breadcrumb Client, ganti isi Search dengan `PT Perpanjang Uji {runId}-195`, tekan Enter
13. Klik Company Name "PT Perpanjang Uji {runId}-195" untuk membuka Detail, lalu buka Tab `Subscription`, sub-tab `FAMS` dan lihat Section "Subscription Details"
14. Verifikasi Status badge `Grace`
15. Verifikasi Grace End terisi
16. Buka Admin Console > Client Subscription dan lakukan Renewal FAMS "PT Perpanjang Uji {runId}-195" yang terotorisasi langsung
17. Tunggu aksi selesai, lalu kembali ke Admin Console > Client > Detail "PT Perpanjang Uji {runId}-195"
18. Klik Tab `Subscription`, sub-tab `FAMS`, dan lihat Section "Subscription Details"
19. Verifikasi Section "Subscription Details" memuat satu ringkasan term (satu Subscription ID) dengan Status badge `Active`
20. Verifikasi status `Grace` dan `Renewed` tidak tampil di sub-tab `FAMS`
21. Verifikasi link `Manage in Client Subscription →` tersedia sebagai jalur ke riwayat term

### TC-AC-ACC-271: Cancel Subscription pada term FAMS Active terakhir: sel FAMS Archive, Client Auto-Archive ke sub-tab Archived, dan tercatat di Changelog

22. Kembali ke List lewat breadcrumb Client, klik sub-tab `Active`, ketik Search `PT Batal Atas Arsip {runId}-195`, tekan Enter
23. Verifikasi sel FAMS baris "PT Batal Atas Arsip {runId}-195" menampilkan badge `Active`
24. Verifikasi sel SAMS dan SIEM baris "PT Batal Atas Arsip {runId}-195" berisi "No Subscription"
25. Klik `[Changelog]` di toolbar List, ketik Search modal `PT Batal Atas Arsip {runId}-195`, tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Auto-Archive` (N1), lalu tutup modal
26. Buka Admin Console > Client Subscription dan Cancel term FAMS yang Active milik "PT Batal Atas Arsip {runId}-195"
27. Tunggu aksi selesai, lalu kembali ke Admin Console > Client, klik sub-tab `Archived`, ketik Search `PT Batal Atas Arsip {runId}-195`, tekan Enter
28. Verifikasi "PT Batal Atas Arsip {runId}-195" tampil di sub-tab `Archived` tanpa aksi manual
29. Verifikasi sel FAMS baris "PT Batal Atas Arsip {runId}-195" menampilkan badge `Archive` (term Active yang di-Cancel masuk `Archive` tanpa melewati `Grace`)
30. Verifikasi badge `Grace` dan `Canceled` tidak tampil pada sel FAMS
31. Klik `[Changelog]` di toolbar List, ketik Search modal `PT Batal Atas Arsip {runId}-195`, tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Auto-Archive` (N2)
32. Verifikasi N2 = N1 + 1
33. Verifikasi baris terbaru Action `Auto-Archive`, Client Name `PT Batal Atas Arsip {runId}-195`, Field `Status`, Old Value `Active`, New Value `Archived`, Modified By `System`

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa aksi pada Client sendiri, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Urutan: Reject (TC-269), Renewal (TC-270, TC-662), lalu Cancel/Auto-Archive (TC-271) di akhir karena membuat Client berpindah ke sub-tab Archived (prinsip 5). Langkah Search, "Tunggu aksi selesai", dan "Kembali ke List" adalah langkah penghubung (S-03, bagian 8b butir 8).
- Temuan untuk QA (S-15): TC-270 hanya menulis "Submit Renewal terotorisasi langsung; Lihat List" dengan Precondition Detail "PT Sejahtera Abadi" (Active), sedangkan judul menyatakan predecessor Expired/Grace; tidak ada fixture yang disebut (C-LIF-7 dipakai TC-662, C-LIF-13 Suspended dipakai TC-673) dan tidak ada nilai sebelum Renewal yang diasersi. Spec memakai Client bersuffix dengan FAMS predecessor Expired (disediakan tim FE/BE) dan perlu dikonfirmasi QA. TC-662 Post Condition (seed ulang C-LIF-7 tanpa syarat) dipenuhi hook `after`.
