---
id: TC-GS-POS-E2E-037-changelog-filter-panel
title: Popup Changelog — Filter Panel (Date, Action, Name, Modified By), Single-day, Kombinasi, Clear Field, Populate vs Hardcode, Loading, Stale Reference, Search Internal Dropdown
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-200
  - TC-GS-POS-208
  - TC-GS-POS-248
  - TC-GS-POS-209
  - TC-GS-POS-254
  - TC-GS-POS-210
  - TC-GS-POS-211
  - TC-GS-POS-212
  - TC-GS-POS-110
  - TC-GS-POS-213
  - TC-GS-POS-214
  - TC-GS-POS-185
coverage:
  web: automated
---

# Popup Changelog — Filter Panel (Date, Action, Name, Modified By)

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Popup Changelog berisi entri log Create/Edit/Delete, minimal beberapa user & beberapa Position. Termasuk skenario untuk stale reference & populate update.
- Filter Panel 4 field: Date (date range), Action (dropdown multi-select searchable), Name (dropdown multi-select searchable, populate dari data Changelog), Modified By (dropdown multi-select searchable, populate dari data Changelog). Field tidak menampilkan Field filter (Single-Value Guard §9.10).

## Test Steps

### A. Screening Filter Panel

1. Buka Popup Changelog → klik Filter → Filter Panel terbuka.
2. Verifikasi field: Date label `"Date"`, placeholder `"Select date range"`.
3. Verifikasi Action: dropdown multi-select searchable, label `"Action"`, placeholder `"All actions"`, opsi `Create, Edit, Delete`.
4. Verifikasi Name: dropdown multi-select searchable, label `"Name"`, placeholder `"All positions"`.
5. Verifikasi Modified By: dropdown multi-select searchable, label `"Modified By"`, placeholder `"All users"`.
6. Verifikasi tombol `[Clear Field]` `[Apply]`.

### B. Filter by Date & single-day

7. Pilih rentang tanggal tertentu → `Apply` → hanya entri tanggal tsb.
8. Clear, buka panel, pilih 1 hari (start==end) → `Apply` → exact match (bukan hari berikutnya).

### C. Filter by Action

9. Pilih Action `Edit` → `Apply` → hanya Action Edit.
10. Action = Create polos (tidak ada qualifier Import) — konfirmasi opsi tetap 3.

### D. Filter by Name & Modified By (populate)

11. Pilih Name tertentu → `Apply` → hanya entri terkait Position tsb.
12. Pilih Modified By tertentu → `Apply` → hanya entri user tsb.

### E. Kombinasi AND antar field & irisan dengan Search

13. Action=`Edit` + Modified By tertentu → `Apply` → AND murni.
14. Search dulu `"Manager"`, baru multi-filter Action+Modified By → `Apply` → hasil = `Search ∩ Multi-Filter`.
15. Multi-filter dulu, baru Search `"Lead"` → `Apply` → hasil = `Multi-Filter ∩ Search`.
16. Kombinasi penuh Search+Multi-Filter+Sort+Pagination → konsisten.

### F. Clear Field & persist state Search

17. Dengan Search+Filter aktif → buka panel, `Clear Field`, `Apply` → filter dilepas, keyword Search tetap aktif.

### G. Populate vs hardcode & update real-time

18. Action hardcode (Create/Edit/Delete). Name/Modified By populate dari data Changelog (bukan master penuh). Opsi Name tidak termasuk Position tanpa entri Changelog.
19. Buat Position baru (Create) → buka kembali Popup Changelog & dropdown Name → opsi baru muncul real-time.
20. Simulasikan loading (opsi fetch lambat) → dropdown menampilkan indikator loading (bukan kosong/prematur).

### H. Stale reference

21. Filter Name = posisi tertentu sedang aktif. Hapus posisi tsb dari master (jika delete-able) → tabel Changelog tetap menampilkan entri historis; saat panel dibuka ulang, opsi tsb hilang dari dropdown Name.

### I. Search internal dropdown

22. Dropdown Action ketik `"ed"` → substring/case-insensitive → hanya `Edit`.
23. Dropdown Name ketik `"hr"` → case-insensitive → match.
24. Dropdown Modified By ketik tidak match → tampil empty state dalam dropdown.

### J. Multi-select OR dalam field & chip removal (2 arah)

25. Action centang Create dan Edit (2 opsi) → closed-state tampil chip terpisah (bukan ringkasan), `Apply` → OR (Create OR Edit).
26. Klik `(X)` pada chip Create (tanpa buka dropdown) → chip Create hilang, checkbox sinkron; `Apply` → hanya Edit.
27. Kembalikan 2 chip, buka dropdown → uncheck Create → chip langsung hilang (sinkron 2 arah checkbox→chip); `Apply` → hanya Edit.
28. Banyak opsi terpilih (≥6) di Modified By → perilaku overflow (chip tersembunyi + indikator `+N more`) terjaga.

## Notes

- Name/Modified By populate scoped ke data Changelog (snapshot historis), bukan live-join penuh ke master data — penting untuk konsistensi historis (stale reference tetap tampil di tabel).
- Action hardcode 3 opsi; qualifier Import tidak menambah opsi terpisah (Create polos).
