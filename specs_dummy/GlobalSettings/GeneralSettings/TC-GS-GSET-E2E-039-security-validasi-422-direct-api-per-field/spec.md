---
id: TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field
title: "Validasi PUT Direct API: 422 per field (Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout) dengan nilai tersimpan tidak berubah"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-133
  - TC-GS-GSET-134
  - TC-GS-GSET-135
  - TC-GS-GSET-136
  - TC-GS-GSET-137
  - TC-GS-GSET-138
  - TC-GS-GSET-139
  - TC-GS-GSET-140
  - TC-GS-GSET-141
  - TC-GS-GSET-142
  - TC-GS-GSET-143
coverage:
  web: automated
---

# Validasi PUT Direct API: 422 per field (Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout) dengan nilai tersimpan tidak berubah

## Prerequisites

- Token sesi aktor Total Control tersedia untuk request API langsung ke `/v2/enterprise-management/general-settings`
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Setiap langkah memakai payload yang valid kecuali satu field yang diuji; setelah tiap request, nilai tersimpan tetap baseline dan tidak ada baris log baru

## Test Steps

### Currency Code

1. Kirim PUT dengan payload valid kecuali currencyCode kosong; verifikasi Response 422 dengan pesan "Currency Code must not be empty"
2. Kirim PUT dengan payload valid kecuali currencyCode `ZZZ`; verifikasi Response 422 dengan pesan "Invalid currency code"

### Time Zone

3. Kirim PUT dengan payload valid kecuali timezone kosong; verifikasi Response 422 dengan pesan "Time Zone must not be empty"
4. Kirim PUT dengan payload valid kecuali timezone `Mars/Olympus`; verifikasi Response 422 dengan pesan "Invalid time zone"
5. Kirim PUT dengan payload valid kecuali timezone `Europe/London` (IANA valid di luar opsi kurasi); verifikasi Response 422 dengan pesan "Invalid time zone" dan timezone tersimpan tetap `Asia/Jakarta`

### Date Format

6. Kirim PUT dengan payload valid kecuali dateFormat kosong; verifikasi Response 422 dengan pesan "Date Format must not be empty"
7. Kirim PUT dengan payload valid kecuali dateFormat `YYYY-MM-DD`; verifikasi Response 422 dengan pesan "Invalid date format"

### Time Format

8. Kirim PUT dengan payload valid kecuali timeFormat kosong; verifikasi Response 422 dengan pesan "Time Format must not be empty"
9. Kirim PUT dengan payload valid kecuali timeFormat `h:mm a`; verifikasi Response 422 dengan pesan "Invalid time format"

### Session Idle Timeout

10. Kirim PUT dengan payload valid kecuali sessionIdleTimeout null; verifikasi Response 422 dengan pesan "Session Idle Timeout must not be empty"
11. Kirim PUT dengan sessionIdleTimeout `45`, lalu `0`, lalu `"Never"`; verifikasi Response 422 dengan pesan "Invalid session idle timeout value"

### Verifikasi Akhir

12. Buka General Settings dan verifikasi kelima nilai tersimpan tetap baseline: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`
13. Buka Modal Changelog dan Activity Log dan verifikasi tidak ada baris log baru dari seluruh request 422 di atas

## Notes

- Spec FE+BE yang hanya mengasersi respons server dan state data. Menggabungkan TC-GS-GSET-133 s.d. 143. Salah satu spec terbesar; assert "tidak ada baris log baru" cukup satu kali di langkah 13.
