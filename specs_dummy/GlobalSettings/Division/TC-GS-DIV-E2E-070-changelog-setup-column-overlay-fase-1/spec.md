---
id: TC-GS-DIV-E2E-070-changelog-setup-column-overlay-fase-1
title: "Setup Column Modal Changelog Fase 1: Overlay Column Visibility 7 Kolom, Toggle Hide/Unhide, dan Guard Kolom Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-213
  - TC-GS-DIV-215
  - TC-GS-DIV-220
coverage:
  web: automated
---

# Setup Column Modal Changelog Fase 1: Overlay Column Visibility 7 Kolom, Toggle Hide/Unhide, dan Guard Kolom Terakhir

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Modal Changelog terbuka
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)

## Test Steps

### Screening Overlay Column Visibility Modal Changelog (TC-GS-DIV-213)

1. Klik icon Changelog di Table Tools
2. Klik header kolom Column Visibility (⋯)
3. Verifikasi Overlay memuat 7 kolom berurutan `Date`, `Action`, `Division Name`, `Field`, `Old Value`, `New Value`, `Modified By` masing-masing tercentang dengan drag handle
4. Verifikasi Item `Setup Column...` di bagian bawah

### Setup Column Modal Changelog: hide dan unhide tiap kolom lalu Save (TC-GS-DIV-215)

5. Klik icon Changelog di Table Tools
6. Buka Popup Setup Column
7. Hilangkan centang `Date` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `Date`
8. Hilangkan centang `Action` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `Action`
9. Hilangkan centang `Division Name` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `Division Name`
10. Hilangkan centang `Field` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `Field`
11. Hilangkan centang `Old Value` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `Old Value`
12. Hilangkan centang `New Value` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `New Value`
13. Hilangkan centang `Modified By` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `Modified By`
14. Setelah kolom terakhir diuji, muat ulang halaman (F5)
15. Verifikasi Date: setelah Save kolom `Date` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
16. Verifikasi Action: setelah Save kolom `Action` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
17. Verifikasi Division Name: setelah Save kolom `Division Name` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
18. Verifikasi Field: setelah Save kolom `Field` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
19. Verifikasi Old Value: setelah Save kolom `Old Value` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
20. Verifikasi New Value: setelah Save kolom `New Value` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
21. Verifikasi Modified By: setelah Save kolom `Modified By` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
22. Verifikasi Setelah F5 konfigurasi terakhir tetap tersimpan

### Setup Column Modal Changelog: kolom visible terakhir tidak dapat di-uncheck (TC-GS-DIV-220)

23. Klik icon Changelog di Table Tools
24. Buka Popup Setup Column
25. Hilangkan centang 6 kolom sehingga tersisa `Date`
26. Hover checkbox `Date`
27. Verifikasi Checkbox `Date` disabled
28. Verifikasi Tooltip: `At least one column must remain visible.`

## Notes

- Memvalidasi Fase 1 Setup Column Modal Changelog (T-DIV-02): screening overlay 7 kolom dengan drag handle dan item Setup Column..., toggle hide/unhide kolom satu per satu dan refleksi ke tabel, serta guard disabled checkbox + tooltip "At least one column must remain visible." saat hanya tersisa 1 kolom (PRD §4.1.2, §4.2e).
- Sumber pemetaan test case granular: TC-GS-DIV-213, TC-GS-DIV-215, TC-GS-DIV-220.
