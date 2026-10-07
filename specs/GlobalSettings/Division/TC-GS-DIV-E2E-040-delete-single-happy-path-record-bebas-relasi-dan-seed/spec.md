---
id: TC-GS-DIV-E2E-040-delete-single-happy-path-record-bebas-relasi-dan-seed
title: "Penghapusan Divisi Bebas Relasi Berhasil (Record Normal dan Seed): Toast Sukses dan Hilang dari Tabel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-116
  - TC-GS-DIV-124
coverage:
  web: automated
---

# Penghapusan Divisi Bebas Relasi Berhasil (Record Normal dan Seed): Toast Sukses dan Hilang dari Tabel

## Prerequisites

- Login sebagai Role: Total Control
- Divisi bebas relasi (Public Relations dan seed bebas relasi Finance)
- User berada di Global Settings > User > Division
- Division `Public Relations` bebas relasi ada (TC-GS-DIV-65)
- Division `Facilities` bebas relasi (TC-GS-DIV-30)

## Test Steps

### Delete Division bebas relasi berhasil (TC-GS-DIV-116)

1. Buka row action baris `Public Relations` lalu klik `Delete`
2. Klik `[Delete]` pada dialog
3. Verifikasi Dialog tertutup
4. Verifikasi Muncul toast sukses: `Success, division has been deleted.`
5. Verifikasi Baris `Public Relations` hilang dari tabel

### Klik ganda Delete hanya memproses satu penghapusan (TC-GS-DIV-124)

6. Buka row action baris `Facilities` lalu klik `Delete`
7. Klik `[Delete]` dua kali cepat
8. Verifikasi Tombol `[Delete]` disabled setelah klik pertama
9. Verifikasi Hanya 1 toast sukses `Success, division has been deleted.` dan 1 entri log Delete

## Notes

- Memvalidasi alur happy path delete single: toast sukses "Success, division has been deleted.", record hilang dari tabel, dan bukti bahwa record seed awal dapat dihapus jika bebas relasi (PRD §3, §9.2).
- Sumber pemetaan test case granular: TC-GS-DIV-116, TC-GS-DIV-124.
