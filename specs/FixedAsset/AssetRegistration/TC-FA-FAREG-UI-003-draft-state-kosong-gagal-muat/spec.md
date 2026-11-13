---
id: TC-FA-FAREG-UI-003-draft-state-kosong-gagal-muat
title: "Sub tab Draft: Loading, empty state, gagal muat, dan Download gagal"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["S-REG-01", "S-REG-07", "S-REG-08", "§4.3#r5", "EB-DL-2@tabel-draft", "EB-TBL-1@tabel-draft"]
smoke: []
dependsOn: []
trace:
  S-REG-01: [2, 3, 4, 8, 9, 10, 11]
  S-REG-07: 14
  S-REG-08: [16, 17]
  "§4.3#r5": [3, 14, 16]
  EB-DL-2@tabel-draft: [22, 26]
  EB-TBL-1@tabel-draft: [3, 8, 12, 16, 18]
coverage:
  web: automated
---

# Sub tab Draft: Loading, empty state, gagal muat, dan Download gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Komponen: Sub tab `Draft` (TBL-REG-01)
- Data:
  - DU-003-1: batch Draft Group `Gudang 1`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-09T08:15:00Z`.
  - DU-003-2: kata kunci Search `Gudang Fiktif` yang tidak cocok dengan batch mana pun.
- Kondisi:
  - K1: daftar Draft kosong, belum ada batch.
  - K2: daftar berisi DU-003-1; pencarian dengan kata kunci DU-003-2 tidak menghasilkan baris.
  - K3: memuat daftar lambat, respons belum selesai.
  - K4: memuat daftar gagal karena error server.
  - K5: daftar berisi DU-003-1; unduhan gagal karena error server.

## Test Steps

### Empty state alami saat belum ada draft
1. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
2. Verifikasi ilustrasi empty state tampil
3. Verifikasi judul empty state `No drafts yet`
4. Verifikasi deskripsi empty state `Get started by creating your first draft.`

### Empty state akibat Search tanpa hasil
5. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
6. Klik ikon Search pada toolbar
7. Ketik Search `Gudang Fiktif`, tekan Enter
8. Verifikasi judul empty state `No results found`
9. Verifikasi deskripsi empty state `Try adjusting your search or filter.`
10. Verifikasi ilustrasi empty state tampil
11. Verifikasi baris `Gudang 1` tidak tampil karena hasil Search tidak cocok
12. Verifikasi judul `No drafts yet` tidak tampil

### Loading berupa shimmer
13. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K3
14. Verifikasi tabel menampilkan `Shimmer`

### Gagal muat bukan empty state
15. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K4
16. Verifikasi pesan `Unable to load this data.`
17. Verifikasi tombol `[Try Again]` tampil
18. Verifikasi judul `No drafts yet` tidak tampil

### Download CSV gagal
19. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K5
20. Klik `Download`
21. Klik `Download as CSV`
22. Verifikasi toast `Error, failed to download Registration-Drafts.`

### Download XLSX gagal
23. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K5
24. Klik `Download`
25. Klik `Download as XLSX`
26. Verifikasi toast `Error, failed to download Registration-Drafts.`
