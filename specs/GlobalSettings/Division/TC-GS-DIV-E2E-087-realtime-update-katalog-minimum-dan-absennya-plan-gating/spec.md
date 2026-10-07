---
id: TC-GS-DIV-E2E-087-realtime-update-katalog-minimum-dan-absennya-plan-gating
title: "Pembaruan Real-Time Tabel, Penjaminan Katalog Minimum 1 Record via In-Use Default User, dan Absennya Plan Gating Seluruh Fitur"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-277
  - TC-GS-DIV-278
  - TC-GS-DIV-279
  - TC-GS-DIV-280
coverage:
  web: automated
---

# Pembaruan Real-Time Tabel, Penjaminan Katalog Minimum 1 Record via In-Use Default User, dan Absennya Plan Gating Seluruh Fitur

## Prerequisites

- Login sebagai Role: Total Control
- Dual tab browser untuk memvalidasi pembaruan real-time (SSE/sync)
- User berada di Global Settings > User > Division
- Tabel Division terbuka di sesi Admin A tanpa Search atau Filter aktif
- Tabel Division terbuka di sesi Admin A dan Division `Realtime Unit` ada (TC-GS-DIV-277)
- Hanya 1 Division tersisa dan dipakai oleh Default User entitas
- Entitas uji tersedia pada plan Starter, Growth, Professional, dan Enterprise

## Test Steps

### Division baru dari admin lain muncul otomatis di tabel yang sedang dibuka (TC-GS-DIV-277)

1. Admin B membuat Division `Realtime Unit` (Code `RTU`)
2. Perhatikan tabel Admin A tanpa reload
3. Verifikasi Baris `Realtime Unit` muncul di tabel Admin A secara diam-diam tanpa dialog
4. Verifikasi Posisi scroll dan halaman aktif Admin A tidak berubah

### Rename Division dari admin lain tampil otomatis di tabel yang sedang dibuka (TC-GS-DIV-278)

5. Admin B mengubah Name `Realtime Unit` menjadi `Realtime Unit 2`
6. Perhatikan tabel Admin A tanpa reload
7. Verifikasi Baris pada tabel Admin A menampilkan `Realtime Unit 2` tanpa reload

### Katalog tidak pernah turun ke nol: Division terakhir otomatis in-use (TC-GS-DIV-279)

8. Centang satu-satunya baris Division
9. Klik aksi `[Delete]` pada Bulk Action Bar
10. Verifikasi Dialog `Cannot Delete Data` tampil dengan bullet `[nama Division] — still in use` dan `[OK]`
11. Verifikasi Division tetap ada sehingga katalog tidak turun ke 0

### Create, Edit, dan Delete identik di semua tier plan tanpa gating (TC-GS-DIV-280)

12. Pada tiap plan: Create Division `Plan Check`, Edit Name menjadi `Plan Check 2`, lalu Delete
13. Verifikasi Starter: Create, Edit, Delete sukses dengan toast sukses masing-masing
14. Verifikasi Growth: sama seperti Starter
15. Verifikasi Professional: sama seperti Starter
16. Verifikasi Enterprise: sama seperti Starter
17. Verifikasi Tidak ada gating, upsell, atau limit berbeda antar plan (hanya Master Data Count Limit platform)

## Notes

- Memvalidasi refleksi instan create/rename dari admin lain ke tabel yang sedang terbuka tanpa refresh, pembuktian katalog minimum 1 record (divisi terakhir otomatis in-use oleh default user, DIV-LOGIC-01c/d), dan ketiadaan pembatasan fitur antar-tier plan langganan (PRD §9.7, §9.10).
- Sumber pemetaan test case granular: TC-GS-DIV-277, TC-GS-DIV-278, TC-GS-DIV-279, TC-GS-DIV-280.
