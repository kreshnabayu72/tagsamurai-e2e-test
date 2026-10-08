---
id: TC-GS-DIV-E2E-025-create-division-master-data-count-limit-guard
title: "Pencegahan Pembuatan Divisi Saat Master Data Count Limit Tercapai: Dialog Blokir pada Klik Toolbar dan Re-Cek Atomik Submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-72
  - TC-GS-DIV-73
  - TC-GS-DIV-74
  - TC-GS-DIV-75
coverage:
  web: automated
---

# Pencegahan Pembuatan Divisi Saat Master Data Count Limit Tercapai: Dialog Blokir pada Klik Toolbar dan Re-Cek Atomik Submit

## Prerequisites

- Login sebagai Role: Total Control
- Master Data Count Limit entitas diatur sama dengan jumlah divisi yang ada saat ini
- User berada di Global Settings > User > Division
- Master Data Count Limit entitas diset sama dengan jumlah Division saat ini (Admin Console > Plans & Licensing > Lifecycle Settings > System Limits)
- Jumlah Division satu di bawah Master Data Count Limit
- Jumlah Division dua di bawah Master Data Count Limit

## Test Steps

### Klik [+ Division] saat Master Data Count Limit tercapai menampilkan Dialog Limit Reached (TC-GS-DIV-72)

1. Perhatikan tombol `[+ Division]`
2. Klik `[+ Division]`
3. Verifikasi Tombol `[+ Division]` tetap Show dan enabled
4. Verifikasi Dialog `Limit Reached` tampil (severity warning) dengan body `You've reached the division limit for this workspace.`
5. Verifikasi Satu tombol `[OK]`; tidak ada modal Create

### Klik OK pada Dialog Limit Reached menutup dialog (TC-GS-DIV-73)

6. Klik `[+ Division]`
7. Klik `[OK]`
8. Verifikasi Dialog `Limit Reached` tertutup
9. Verifikasi Tidak ada toast dan tidak ada modal Create; tabel tidak berubah

### Limit tercapai saat Submit menolak Create dengan Dialog Limit Reached (TC-GS-DIV-74)

10. Klik `[+ Division]` dan isi Division Name `Archive Unit` serta Code `ARC`
11. Admin lain membuat 1 Division sehingga limit tercapai
12. Klik `[Submit]`
13. Verifikasi Dialog `Limit Reached` yang sama tampil dengan body `You've reached the division limit for this workspace.`
14. Verifikasi Record `Archive Unit` tidak dibuat
15. Verifikasi Modal Create tetap terbuka dengan Division Name dan Code dipertahankan

### Create berulang dengan Stay checked sampai limit: data terakhir berhasil, berikutnya ditolak (TC-GS-DIV-75)

16. Klik `[+ Division]` dan centang `Stay on this form after submitting`
17. Submit Division `Billing` (Code `BIL`)
18. Submit Division `Collections` (Code `COL`)
19. Submit Division `Disputes` (Code `DSP`)
20. Verifikasi Division `Billing` dan `Collections` berhasil dibuat dengan toast sukses `Success, division has been created.` dan form tetap terbuka ter-reset
21. Verifikasi Submit `Disputes` ditolak dengan Dialog `Limit Reached`; record tidak dibuat; form tetap terbuka dengan input dipertahankan

## Notes

- Memvalidasi Dialog 6 Limit Reached (D-06: "You've reached the division limit for this workspace." + tombol tunggal [OK]) saat klik toolbar maupun saat re-cek atomik di submit (PRD §4.2d, §6 V-08, §9.5).
- Sumber pemetaan test case granular: TC-GS-DIV-72, TC-GS-DIV-73, TC-GS-DIV-74, TC-GS-DIV-75.
