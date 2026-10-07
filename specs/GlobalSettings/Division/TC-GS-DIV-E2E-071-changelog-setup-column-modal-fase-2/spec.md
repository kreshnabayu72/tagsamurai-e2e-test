---
id: TC-GS-DIV-E2E-071-changelog-setup-column-modal-fase-2
title: "Setup Column Modal Changelog Fase 2: Modal Setup Column, Drag-and-Drop Reorder 7 Kolom, dan Freeze Pinning Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-214
  - TC-GS-DIV-216
  - TC-GS-DIV-217
coverage:
  web: automated
---

# Setup Column Modal Changelog Fase 2: Modal Setup Column, Drag-and-Drop Reorder 7 Kolom, dan Freeze Pinning Kolom

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Modal Changelog terbuka
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)

## Test Steps

### Screening Popup Setup Column Modal Changelog (TC-GS-DIV-214)

1. Klik icon Changelog di Table Tools
2. Klik header Column Visibility (⋯)
3. Klik `[Setup Column]`
4. Verifikasi Title `Setup Column`
5. Verifikasi Subtitle `Manage column visibility, reorder, and freeze columns.`
6. Verifikasi Icon close `[✕]`
7. Verifikasi Daftar 7 kolom tercentang dengan drag handle dan icon pin
8. Verifikasi Preview tabel Changelog
9. Verifikasi `[Reset to Default]` dan `[Save]`

### Setup Column Modal Changelog: reorder tiap kolom lewat drag lalu Save (TC-GS-DIV-216)

10. Klik icon Changelog di Table Tools
11. Buka Popup Setup Column
12. Seret `Date` ke posisi pertama, klik `[Save]`, lihat tabel
13. Seret `Action` ke posisi pertama, klik `[Save]`, lihat tabel
14. Seret `Division Name` ke posisi pertama, klik `[Save]`, lihat tabel
15. Seret `Field` ke posisi pertama, klik `[Save]`, lihat tabel
16. Seret `Old Value` ke posisi pertama, klik `[Save]`, lihat tabel
17. Seret `New Value` ke posisi pertama, klik `[Save]`, lihat tabel
18. Seret `Modified By` ke posisi pertama, klik `[Save]`, lihat tabel
19. Verifikasi Date: setelah Save kolom `Date` berada di posisi pertama tabel
20. Verifikasi Action: setelah Save kolom `Action` berada di posisi pertama tabel
21. Verifikasi Division Name: setelah Save kolom `Division Name` berada di posisi pertama tabel
22. Verifikasi Field: setelah Save kolom `Field` berada di posisi pertama tabel
23. Verifikasi Old Value: setelah Save kolom `Old Value` berada di posisi pertama tabel
24. Verifikasi New Value: setelah Save kolom `New Value` berada di posisi pertama tabel
25. Verifikasi Modified By: setelah Save kolom `Modified By` berada di posisi pertama tabel
26. Verifikasi Setelah F5 urutan terakhir tetap tersimpan

### Setup Column Modal Changelog: pin dan unpin tiap kolom lalu Save (TC-GS-DIV-217)

27. Klik icon Changelog di Table Tools
28. Buka Popup Setup Column
29. Klik icon pin pada `Date`, klik `[Save]`, scroll tabel horizontal, lalu unpin `Date` dan Save
30. Klik icon pin pada `Action`, klik `[Save]`, scroll tabel horizontal, lalu unpin `Action` dan Save
31. Klik icon pin pada `Division Name`, klik `[Save]`, scroll tabel horizontal, lalu unpin `Division Name` dan Save
32. Klik icon pin pada `Field`, klik `[Save]`, scroll tabel horizontal, lalu unpin `Field` dan Save
33. Klik icon pin pada `Old Value`, klik `[Save]`, scroll tabel horizontal, lalu unpin `Old Value` dan Save
34. Klik icon pin pada `New Value`, klik `[Save]`, scroll tabel horizontal, lalu unpin `New Value` dan Save
35. Klik icon pin pada `Modified By`, klik `[Save]`, scroll tabel horizontal, lalu unpin `Modified By` dan Save
36. Verifikasi Date: kolom `Date` membeku (sticky) saat scroll horizontal setelah Save
37. Verifikasi Action: kolom `Action` membeku (sticky) saat scroll horizontal setelah Save
38. Verifikasi Division Name: kolom `Division Name` membeku (sticky) saat scroll horizontal setelah Save
39. Verifikasi Field: kolom `Field` membeku (sticky) saat scroll horizontal setelah Save
40. Verifikasi Old Value: kolom `Old Value` membeku (sticky) saat scroll horizontal setelah Save
41. Verifikasi New Value: kolom `New Value` membeku (sticky) saat scroll horizontal setelah Save
42. Verifikasi Modified By: kolom `Modified By` membeku (sticky) saat scroll horizontal setelah Save
43. Verifikasi Setelah F5 pin terakhir yang disimpan tetap berlaku

## Notes

- Memvalidasi Fase 2 Setup Column Modal Changelog: screening dialog Setup Column, drag-and-drop reorder urutan 7 kolom dan verifikasi perubahan urutan di tabel, serta icon pin untuk membekukan kolom (sticky freeze) saat scroll tabel horizontal (PRD §4.1.2, §4.2e).
- Sumber pemetaan test case granular: TC-GS-DIV-214, TC-GS-DIV-216, TC-GS-DIV-217.
