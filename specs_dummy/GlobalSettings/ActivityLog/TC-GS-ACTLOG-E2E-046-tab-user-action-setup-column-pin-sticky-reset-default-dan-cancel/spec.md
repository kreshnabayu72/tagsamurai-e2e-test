---
id: TC-GS-ACTLOG-E2E-046-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel
title: "Tab User Action Setup Column: Pembekuan Kolom Sticky Pin/Unpin, Batas 3 Kolom, dan Reset"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-185
  - TC-GS-ACTLOG-186
  - TC-GS-ACTLOG-187
  - TC-GS-ACTLOG-188
coverage:
  web: automated
---

# Tab User Action Setup Column: Pembekuan Kolom Sticky Pin/Unpin, Batas 3 Kolom, dan Reset

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Viewport diatur sehingga tabel Tab User Action dapat digulir horizontal

## Test Steps

### Pin dan Unpin Kolom
1. Buka popup Setup Column, klik icon Pin pada kolom 'Date', klik [Save].
2. Gulir tabel horizontal ke kanan, verifikasi kolom Date membeku di sisi kiri tabel.
3. Refresh browser (F5), verifikasi kolom Date tetap dalam keadaan ter-pin.
### Pin 3 Kolom Sekaligus
4. Buka kembali popup Setup Column, aktifkan pin pada kolom 'Action' dan 'Object' (total 3 kolom: Date, Action, Object).
5. Seret kolom Object ke posisi paling kiri di antara kelompok kolom beku, klik [Save].
6. Gulir tabel ke kanan: verifikasi ketiga kolom membeku di sisi kiri dengan urutan Object, Date, Action.
### Penolakan Pin Kolom ke-4 (Batas Maksimal 3 Kolom)
7. Buka kembali popup Setup Column saat 3 kolom sudah ter-pin.
8. Amati icon Pin pada baris kolom 'Name'.
9. Verifikasi icon Pin kolom Name berstatus disabled dan tidak dapat diklik.
10. Arahkan kursor ke icon Pin tersebut, verifikasi muncul tooltip 'Maximum 3 columns can be pinned at once. Unpin another column first.'.
11. Klik icon Pin pada kolom Date untuk melepas pin.
12. Verifikasi icon Pin pada kolom Name otomatis kembali aktif.
### Reset to Default
13. Klik tombol [Reset to Default] di modal popup.
14. Verifikasi seluruh pin terlepas dan susunan kembali ke default tanpa kolom beku.
15. Klik [Save], verifikasi tabel kembali normal.

## Notes

- Fitur sticky pin dibatasi maksimal 3 kolom untuk menjaga proporsi visual tabel.
