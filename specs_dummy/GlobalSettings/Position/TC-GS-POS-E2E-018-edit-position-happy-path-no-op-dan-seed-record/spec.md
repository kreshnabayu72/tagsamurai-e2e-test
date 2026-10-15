---
id: TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record
title: "Edit Position sukses rename, kapitalisasi, No-Op tanpa log/update, 1 karakter, 120 karakter, dan record seed"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-79
  - TC-GS-POS-89
  - TC-GS-POS-90
  - TC-GS-POS-91
  - TC-GS-POS-92
  - TC-GS-POS-110
  - TC-GS-POS-283
  - TC-GS-POS-287
coverage:
  web: automated
---

# Edit Position sukses rename, kapitalisasi, No-Op tanpa log/update, 1 karakter, 120 karakter, dan record seed

## Prerequisites

- Login sebagai Role: Total Control
- Record "IT Support Specialist" dan record seed entitas "Head of Operations" tersedia

## Test Steps

### Rename Sukses dan Batas Karakter

1. Buka modal Edit pada record "IT Support Specialist"
2. Ubah nama menjadi batas 1 karakter "B" lalu klik "[Save]"
3. Verifikasi toast sukses muncul dan nama di tabel terbarukan
4. Buka kembali modal Edit pada record tersebut, ubah nama menjadi batas tepat 120 karakter
5. Klik "[Save]" dan verifikasi simpan berhasil
6. Buka kembali modal Edit dan ubah nama menjadi "IT Operations Lead"
7. Klik "[Save]", verifikasi toast sukses muncul dan nama di tabel terupdate

### Perubahan Kapitalisasi Sah

8. Buka modal Edit pada "IT Operations Lead", ubah menjadi "it operations lead" (huruf kecil semua)
9. Klik "[Save]", verifikasi perubahan kapitalisasi diterima dan tercatat sebagai Edit yang sah

### No-Op Submission

10. Buka kembali modal Edit pada "it operations lead", tanpa mengubah nilai klik "[Save]"
11. Verifikasi modal tertutup, tidak ada toast error, dan timestamp Last Updated tidak berubah (No-Op)
12. Buka modal Edit, tambahkan spasi "  it operations lead  ", klik "[Save]"
13. Verifikasi diperlakukan sebagai No-Op karena trimmed name tidak berubah

### Edit Record Seed

14. Buka menu ⋯ pada record seed "Head of Operations", verifikasi menu Edit dan Delete tersedia normal
15. Klik "Edit", ubah menjadi "Head of Global Operations", klik "[Save]"
16. Verifikasi record seed berhasil di-edit seperti record biasa

## Notes

- Menggabungkan TC-GS-POS-79, 89, 90, 91, 92, 110, 283, dan 287.
